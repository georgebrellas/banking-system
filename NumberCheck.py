#Credits to stackoverflow for the number check function!
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
