import math
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
SPEEDBUMP = 1.0
MAX_VOLUME = 20000
MAX_ORDERS = 1
SPREAD = .01

#Returns the 'tick' of the running case.
def get_tick(session):
    resp = session.get('http://localhost:10002/v1/case')
    if resp.ok:
        case = resp.json()
        return case ['tick']
    raise ApiException('Authorization Error, Please check API Key.')

#This returns the bid and ask first row for a given security
def ticker_bid_ask(session, ticker):
    payload = {'ticker': ticker}
    resp = session.get('http://localhost:10002/v1/securities/book', params = payload)
    if resp.ok:
        book = resp.json()
        return book['bids'][0]['price'], book['asks'][0]['price']
    raise ApiException('Authorization error, Please check API key.')

def inventory(session, ticker):
    payload = {'ticker': ticker}
    resp = session.get('http://localhost:10002/v1/securities', params = payload)
    if resp.ok:
        inventory = resp.json()
        return inventory[0]['position']
    raise ApiException('Authorization error, Please check API key.')

#Returns information on all open sell orders
def open_sells(session):
    resp = session.get('http://localhost:10002/v1/orders?status=OPEN')
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
    resp = session.get('http://localhost:10002/v1/orders?status=OPEN')
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
        session.post('http://localhost:10002/v1/orders', params = {'ticker': 'THOR_M','type': 'LIMIT', 'quantity': MAX_VOLUME, 'price': sell_price, 'action':'SELL'})
        session.post('http://localhost:10002/v1/orders', params = {'ticker': 'THOR_M','type': 'LIMIT', 'quantity': MAX_VOLUME, 'price': buy_price, 'action':'BUY'})

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
        deleted = session.delete('http://localhost:10002/v1/orders/{}'.format(id))
        if(deleted.ok):
            session.post('http://localhost:10002/v1/orders', params= {'ticker':'THOR_M', 'type': 'LIMIT', 'quantity': volume, 'price': price, 'action': action})

def get_tenders(session):
    tenders_list = []
    resp = session.get('http://localhost:10002/v1//tenders')
    if resp.ok:
        tender_id = 0
        expiry = 0
        tender_ticker = 0
        tender_quantity = 0
        tender_action = []
        tender_price = 0

        tenders = resp.json()
        if len(tenders) != 0:
            tender_id = tenders[0]['tender_id']
            expiry = tenders[0]['expires']
            tender_ticker = tenders[0]['ticker']
            tender_quantity = tenders[0]['quantity']
            tender_action = tenders[0]['action']
            tender_price = tenders[0]['price']
    return tender_id, expiry, tender_ticker, tender_quantity, tender_action, tender_price

def picker():

    lowest_price = min(bid_price_A,bid_price_M)
    highest_price = max(ask_price_A,ask_price_M)

    if bid_price_A < bid_price_M:
        buyticker = 'THOR_A'
    else:
        buyticker = 'THOR_M'

    if ask_price_A > ask_price_M:
        sellticker = 'THOR_A'
    else:
        sellticker = 'THOR_M'
    return buyticker,sellticker,lowest_price,highest_price

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

    tender_id = []
    expiry = []
    tender_ticker = []
    tender_quantity = []
    tender_action = []
    tender_price = []

    single_side_filled = False
    single_side_transaction_time = 0
    #stocks = [CNR,ALG,AC]
#creates session to manage connections
with requests.Session() as s:
    s.headers.update(API_KEY)
    tick = get_tick(s)

    #While time is between 2 and 298, do the following:
    while tick > 2 and tick < 298 and not shutdown:
        #This updates information about the case 
        #We call open_sells (defined above) to assign the output to the variables.
        volume_filled_sells, open_sells_volume, sell_ids, sell_prices, sell_volumes = open_sells(s)
        volume_filled_buys, open_buys_volume, buy_ids, buy_prices, buy_volumes = open_buys(s)
        bid_price_M, ask_price_M = ticker_bid_ask(s, 'THOR_M')
        bid_price_A, ask_price_A = ticker_bid_ask(s, 'THOR_A')
        buyticker, sellticker, lowest_price, highest_price  = picker()
        tender_id, expiry, tender_ticker, tender_quantity, tender_action, tender_price = get_tenders(s)
        stockinventory = inventory(s,'THOR_M')

        if stockinventory < 0:
            picker()
            print('Time to buy')
            bucket = math.trunc(stockinventory/10000)
            bucket = abs(bucket)
            print(bucket)
            bucketrem = (stockinventory/10000) - bucket
            bucketrem = abs(bucketrem)
            print(bucketrem)
            sleep(SPEEDBUMP)
            while bucket > 0:
                picker()
                s.post('http://localhost:10002/v1/orders', params = {'ticker': buyticker,'type': 'MARKET', 'quantity': 10000, 'action':'BUY'})
                bucket = bucket - 1
                print(bucket)
                sleep(SPEEDBUMP)
            while bucketrem > 0:
                picker()
                s.post('http://localhost:10002/v1/orders', params = {'ticker': buyticker,'type': 'MARKET', 'quantity': bucketrem * 10000, 'action':'BUY'})
                bucketrem = bucketrem - bucketrem
                print(bucketrem)
                print('0 Position')
                sleep(SPEEDBUMP)
                break
        else:
            pass

        if stockinventory > 0:
            picker()
            bucket = math.trunc(stockinventory/10000)
            bucketrem = (stockinventory/10000) - bucket
            while bucket > 0:
                s.post('http://localhost:10002/v1/orders', params = {'ticker': sellticker,'type': 'MARKET', 'quantity': 10000, 'action':'SELL'})
                bucket = bucket - 1
                print(bucket)
                sleep(SPEEDBUMP)
            while bucketrem > 0:
                s.post('http://localhost:10002/v1/orders', params = {'ticker': sellticker,'type': 'MARKET', 'quantity': bucketrem * 10000, 'action':'SELL'})
                bucketrem = bucketrem - bucketrem
                print('Sold rest to market')
                sleep(SPEEDBUMP)
                break
        else:
            pass

        if tender_id > 0:
            picker()
            print('we have a tender!')
            if tender_action == 'SELL':
                print('Buy')
                print(tender_price)
                print(lowest_price)
                if tender_price > lowest_price:
                    print('the tender price is higher than the lowest price on the market')
                    bucket = math.trunc(tender_quantity/10000)
                    bucketrem = (tender_quantity/10000) - bucket
                    while bucket > 0:
                        picker()
                        s.post('http://localhost:10002/v1/orders', params = {'ticker': buyticker,'type': 'MARKET', 'quantity': 10000, 'action':'BUY'})
                        bucket = bucket - 1
                        print(bucket)
                        sleep(SPEEDBUMP)
                    while bucketrem > 0:
                        picker()
                        s.post('http://localhost:10002/v1/orders', params = {'ticker': buyticker,'type': 'MARKET', 'quantity': bucketrem * 10000, 'action':'BUY'})   
                        s.post('http://localhost:10002/v1/tenders/{}'.format(tender_id))
                        bucketrem = bucketrem - bucketrem
                        print('Sold rest to market')
                        sleep(SPEEDBUMP)
                        break
                    sleep(SPEEDBUMP)
            else:
                picker()
                print('Sell')
                if tender_price < highest_price:
                    bucket = math.trunc(tender_quantity/10000)
                    bucketrem = (tender_quantity/10000) - bucket
                    print(sellticker)
                    while bucket > 0:
                        picker()
                        s.post('http://localhost:10002/v1/orders', params = {'ticker': sellticker,'type': 'MARKET', 'quantity': 10000, 'action':'SELL'})
                        bucket = bucket - 1
                        print(bucket)
                        sleep(SPEEDBUMP)
                    while bucketrem > 0:
                        picker()
                        s.post('http://localhost:10002/v1/orders', params = {'ticker': sellticker,'type': 'MARKET', 'quantity': bucketrem * 10000, 'action':'SELL'})
                        print(bucketrem)
                        bucketrem = bucketrem - bucketrem
                        print(bucketrem)
                        print('Everything Sold')
                        s.post('http://localhost:10002/v1/tenders/{}'.format(tender_id))
                        sleep(SPEEDBUMP)
                        break
                    sleep(SPEEDBUMP)
        tick = get_tick(s)
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()

