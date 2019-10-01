import re

def is_color(string):
    if re.match(r'^[a-zA-Z ]*$', string):
        if not string.isspace() and string != '':
            pass
        else:
            colour = input('invalid color name please give correct input : ')
            return is_color(colour)
    else:
        colour = input('invalid color name please give correct input : ')
        return is_color(colour)
    return string


def is_vehicle_number(string):
    if string.isalnum():
        pass
    else:
        number = input('invalid number please give correct input : ')
        return is_vehicle_number(number)
    return string