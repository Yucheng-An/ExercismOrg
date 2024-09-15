EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    '''
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    '''

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    '''
    :param number_of_layers: int number of layers in the lasagna
    :return: int time to prepare the lasagna

    Function that calculates the time of preparation according to the number of
    layers.
    '''

    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''
    :param number_of_layers: int number of layers in the lasagna
    :param elapsed_bake_time: int baking time already elapsed
    :return: int baking time elapsed in minutes

    Function that calculates the elapsed time in minutes according to the number
    of layers and elapsed bake time.
    '''

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time