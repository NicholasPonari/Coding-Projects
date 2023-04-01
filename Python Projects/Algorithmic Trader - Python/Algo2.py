import signal
import requests
from time import sleep
import sys

# Prints error messages and stops the program
class ApiException(Exception):
    pass

#Shutsdown when CTRL+C is pressed
def signal_handler(signum, frame):
    global shutdown
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    shutdown = True

#API Key is set here to connect to trader
API_KEY = {'X-API-Key': '48EHJRRZ'}
shutdown = False

#Settings
SPEEDBUMP = 0.3
MAX_VOLUME = 5000
MAX_ORDERS = 5
SPREAD = .010

#Returns the 'tick' of the running case.
def get_tick(session):
    resp = session.get('http://localhost:10000/v1/case')
    if resp.ok:
        case = resp.json()
        return case ['tick']
    raise ApiException('Authorization Error, Please check API Key.')

#This returns the bid and ask first row for a given security
def ticker_bid_ask(session, ticker):
    payload = {'ticker': ticker}
    resp = session.get('http://localhost:10000/v1/securities/book', params = payload)
    if resp.ok:
        book = resp.json()
        return book['bids'][0]['price'], book['asks'][0]['price']
    raise ApiException('Authorization error, Please check API key.')

#Returns information on all open sell orders
def open_sells(session):
    resp = session.get('http://localhost:10000/v1/orders?status=OPEN')
    if resp.ok:
        open_sells_volume = 0 #total combined volume of all open sells
        ids = []
        prices = []
        order_volumes = []
        volume_filled = []

        #resp.json holds the information from the RIT Trader
        open_orders = resp.json()
        #we iterate through all the orders in the JSON
        for order in open_orders:
            #if the order's action is "sell", do the following
            if order['action'] == 'SELL':
                #volume_filled is a list, we append the quantity filled from the JSON
                volume_filled.append(order['quantity_filled'])
                #order_volumes is a list defined above, we add the quantity still open
                order_volumes.append(order['quantity'])
                #open sells volume is itself plus the quantity still open
                open_sells_volume = open_sells_volume + order['quantity']
                #we add the price to a list called "prices"
                prices.append(order['price'])
                #lastly we add the order IDs
                ids.append(order['order_id'])
    return volume_filled, open_sells_volume, ids, prices, order_volumes

#Returns information on all open buy orders
def open_buys(session):
    resp = session.get('http://localhost:10000/v1/orders?status=OPEN')
    if resp.ok:
        open_buys_volume = 0
        ids = []
        prices = []
        order_volumes = []
        volume_filled = []

        open_orders = resp.json()
        for order in open_orders:
            if order['action'] == 'BUY':
                open_buys_volume = open_buys_volume + order['quantity']
                volume_filled.append(order['quantity_filled'])
                order_volumes.append(order['quantity'])
                prices.append(order['price'])
                ids.append(order['order_id'])
    return volume_filled, open_buys_volume, ids, prices, order_volumes

#this function buys and sells shares according to what we put in MAX_ORDERS at the beginning
def buy_sell(session, sell_price, buy_price):
    for i in range(MAX_ORDERS):
        session.post('http://localhost:10000/v1/orders', params = {'ticker': 'ALGO','type': 'LIMIT', 'quantity': MAX_VOLUME, 'price': sell_price, 'action':'SELL'})
        session.post('http://localhost:10000/v1/orders', params = {'ticker': 'ALGO','type': 'LIMIT', 'quantity': MAX_VOLUME, 'price': buy_price, 'action':'BUY'})

#this function re-orders all open buys or sells
def re_order(session, number_of_orders, ids, volumes_filled, volumes, price, action):
    for i in range(number_of_orders):
        id = ids[i]
        volume = volumes[i]
        volume_filled = volumes_filled[i]
        #This is meant to deal with partial fills
        if(volume_filled != 0):
            volume = MAX_VOLUME - volume_filled
        #delete and then repurchase
        deleted = session.delete('http://localhost:10000/v1/orders/{}'.format(id))
        if(deleted.ok):
            session.post('http://localhost:10000/v1/orders', params= {'ticker':'ALGO', 'type': 'LIMIT', 'quantity': volume, 'price': price, 'action': action})

def main():
    buy_ids = []
    buy_prices = []
    buy_volumes = []
    volume_filled_buys = []
    open_buys_volume = 0

    sell_ids = []
    sell_prices = []
    sell_volumes = []
    volume_filled_sells = []
    open_sells_volume = 0

    single_side_filled = False
    single_side_transaction_time = 0
    #stocks = [CNR,ALG,AC]
#creates session to manage connections
with requests.Session() as s:
    s.headers.update(API_KEY)
    tick = get_tick(s)

    #While time is between 5 and 295, do the following:
    while tick > 2 and tick < 298 and not shutdown:
        #This updates information about the case 
        #We call open_sells (defined above) to assign the output to the variables.
        volume_filled_sells, open_sells_volume, sell_ids, sell_prices, sell_volumes = open_sells(s)
        volume_filled_buys, open_buys_volume, buy_ids, buy_prices, buy_volumes = open_buys(s)
        bid_price, ask_price = ticker_bid_ask(s, 'ALGO')       

        #Check if there's no open orders
        if (open_sells_volume == 0 and open_buys_volume == 0):
            #bost sides are filled now
            single_side_filled = False
            #Calculate the spread between the bid and ask price
            bid_ask_spread = ask_price - bid_price
            #set the prices so sell = ask and buy = bid so we get best possible prices
            sell_price = ask_price
            buy_price = bid_price

            #The calculated spread is greater or equal to the spread we set
            if(bid_ask_spread >= SPREAD):
                #buy and sell the maximum number of shares
                buy_sell(s, sell_price, buy_price)
                sleep(SPEEDBUMP)

        #What if there ARE outstanding open orders?
        else:
            #one side of the book has no open orders
            if(not single_side_filled and (open_buys_volume == 0 or open_sells_volume == 0)):
                single_side_filled = True
                single_side_transaction_time = tick
                
            #ask side is completely filled
            if(open_sells_volume == 0):
                #and IF the current buy orders are at the top of the book
                if(buy_price == bid_price):
                    #Just chillax and go forward
                    continue
                #otherwise, it's been more than 3 seconds since a side has been filled
                elif(tick - single_side_transaction_time >= 3):
                    #calculate the potential profits
                    next_buy_price = bid_price + .01
                    potential_profit = sell_price - next_buy_price - .02

                    #if potential profits are more than a cent or it's been more than 5 seconds
                    if(potential_profit >= .01 or tick - single_side_transaction_time >= 5):
                        action = 'BUY'
                        number_of_orders = len(buy_ids)
                        buy_price = bid_price + .01
                        price = buy_price
                        ids = buy_ids
                        volumes = buy_volumes
                        volumes_filled = volume_filled_buys
                        #Set new settings and delete buys and rebuy with new paramters
                        re_order(s, number_of_orders, ids, volumes_filled, volumes, price, action)
                        sleep(SPEEDBUMP)
                
            elif(open_buys_volume == 0):
                if(sell_price == ask_price):
                    continue
                elif(tick - single_side_transaction_time >= 3):
                    next_sell_price = ask_price - .01
                    potential_profit = next_sell_price - buy_price - .02

                    if(potential_profit >= .01 or tick - single_side_transaction_time >= 5):
                        action = 'SELL'
                        number_of_orders = len(sell_ids)
                        sell_price = ask_price - .01
                        price = sell_price
                        ids = sell_ids
                        volumes = sell_volumes
                        volumes_filled = volume_filled_sells
                        re_order(s, number_of_orders, ids, volumes_filled, volumes, price, action)
                        sleep(SPEEDBUMP)

        #refreshes the case time, this is hyper important for the WHILE loop      
        tick = get_tick(s)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()