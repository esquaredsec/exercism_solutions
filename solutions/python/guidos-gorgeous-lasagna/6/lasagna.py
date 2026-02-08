EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining."""
    result = EXPECTED_BAKE_TIME - elapsed_bake_time
    return result

# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the bake time remaining."""
    layer_prep = 2
    result = number_of_layers * layer_prep  
    return result

# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time."""
    result = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return result
    