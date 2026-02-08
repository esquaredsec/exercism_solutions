"""Functions used in preparing Guido's gorgeous lasagna."""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining."""
    result = EXPECTED_BAKE_TIME - elapsed_bake_time
    return result

def preparation_time_in_minutes(number_of_layers):
    """Calculate the bake time remaining."""
    layer_prep = 2
    result = number_of_layers * layer_prep  
    return result

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time."""
    result = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return result
    