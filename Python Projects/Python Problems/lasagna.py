"""Functions used in preparing Guido's gorgeous lasagna.
 
Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""
EXPECTED_BAKE_TIME = 40
def bake_time_remaining(elapsed_bake_time):
    """
    Returns how much time is remaining to bake the lasagna. This function takes an argument (elapsed time) and uses it to subtract that value from the total expected time to return the time remaining.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(number_of_layers):
    """
    Return elapsed cooking time. This function takes two numbers representing the number of layers & the time already spent baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return number_of_layers * 2
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time. This function takes two numbers representing the number of layers & the time already spent baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
