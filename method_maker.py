def print_history(_history):
    """This function prints the history of all the bells in a human readable form."""
    for change in _history:
        print(' '.join(str(bell) for bell in change))


def swap(change, i, j):
    """Swaps two bells over. This is equivalent to a called change if it is the only thing
    going on."""
    change[i], change[j] = change[j], change[i]


def do_places_group(change, places_group):
    """This does the swaps required to implement a single change of place notation."""
    if 'x' in places_group:
        # x is used to mark changes with no constant bells
        constant_places = []
    else:
        constant_places = [int(place)-1 for place in places_group]
    change = change.copy()
    i = 0
    while i < len(change)-1:
        if i in constant_places:
            i += 1
        else:
            swap(change, i, i+1)
            i += 2
    return change


def execute_place_notation(_history, place_notation):
    """This does the sequence of swaps required for a method"""
    for places in place_notation.split(' '):
        if places:
            _history.append(do_places_group(_history[-1], places))
    return _history


start = [1, 2, 3, 4, 5, 6]
dodging = 'x ' * 100
plain_hunt_minor = 'x 1 ' * 6
plain_hunt_doubles = '5 1 ' * 5
bob_doubles_lead = '5 1 ' * 4 + '5 125 '
bob_doubles_plain_course = bob_doubles_lead * 4
history = execute_place_notation([start], bob_doubles_plain_course)
print_history(history)


