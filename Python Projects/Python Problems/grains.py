def square(number):
    if number > 0 and number < 65:
       return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")
        
def total():
    return (2 ** 64) - 1