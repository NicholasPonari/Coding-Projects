# Score categories.
# category calls a lambda function
YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = lambda dice: 1 * dice.count(1) 
TWOS = lambda dice: 2 * dice.count(2)
THREES = lambda dice: 3 * dice.count(3)
FOURS = lambda dice: 4 * dice.count(4)
FIVES = lambda dice: 5 * dice.count(5)
SIXES = lambda dice: 6 * dice.count(6)
FULL_HOUSE = lambda dice: sum(dice) if len(set(dice)) == 2 and any(dice.count(x) == 3 for x in set(dice)) else 0
FOUR_OF_A_KIND = lambda dice: sum(x * 4 for x in set(dice) if dice.count(x) >= 4)
LITTLE_STRAIGHT = lambda dice: 30 if sum(dice) == 15 and len(set(dice)) == 5 else 0
BIG_STRAIGHT = lambda dice: 30 if sum(dice) == 20 and len(set(dice)) == 5 else 0
CHOICE = lambda dice: sum(dice)

def score(dice, category):
    return category(dice)
