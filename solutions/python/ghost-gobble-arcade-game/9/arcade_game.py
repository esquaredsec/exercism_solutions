"""Functions for implementing the rules of the classic arcade game Pac-Man."""

def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet."""
    while power_pellet_active and touching_ghost:
        return True
    return False

def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten."""
    while touching_dot or touching_power_pellet:
        return True
    return False
    
def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet."""
    while touching_ghost and power_pellet_active is False:
        return True
    return False


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten."""
    if touching_ghost is True and power_pellet_active is False or has_eaten_all_dots is False:
        return False
    return True