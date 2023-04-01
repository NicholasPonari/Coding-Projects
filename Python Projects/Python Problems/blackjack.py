def value_of_card(card):
    if card in ['J','Q','K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)
def higher_card(card_one, card_two):
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    if card_one_value == card_two_value:
        return card_one, card_two
    elif card_one_value > card_two_value:
        return card_one
    else:
        return card_two
def value_of_ace(card_one, card_two):
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    if card_one == 'A' or card_two == 'A':
        return 1
    elif card_one_value + card_two_value <= 10:
        return 11
    else:
        return 1
def real_value_of_ace(card_one, card_two):
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    if card_one == 'A' or card_two == 'A':
        return 11
    elif card_one_value + card_two_value <= 10:
        return 1
    else:
        return 11
def is_blackjack(card_one, card_two):
    if card_one == 'A':
        card_one_value = real_value_of_ace(card_one, card_two)
        card_two_value = value_of_card(card_two)
    elif card_two == 'A':
        card_two_value = real_value_of_ace(card_one, card_two)
        card_one_value = value_of_card(card_one)
    else:
        card_one_value = value_of_card(card_one)
        card_two_value = value_of_card(card_two)
    
    if card_one_value + card_two_value == 21:
        return True
    else:
        return False
    
def can_split_pairs(card_one, card_two):
    if card_one == 'A' and card_two == 'A':
        return True
    elif card_one == 'A':
        card_one_value = real_value_of_ace(card_one, card_two)
        card_two_value = value_of_card(card_two)
    elif card_two == 'A':
        card_two_value = real_value_of_ace(card_one, card_two)
        card_one_value = value_of_card(card_one)
    else:
        card_one_value = value_of_card(card_one)
        card_two_value = value_of_card(card_two)
    if card_one_value == card_two_value:
        return True
    else:
        return False
def can_double_down(card_one, card_two):
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    
    hand_value = card_one_value + card_two_value
    
    if hand_value in [9,10,11]:
        return True
    else:
        return False
