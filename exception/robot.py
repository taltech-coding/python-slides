class TooYoungToEnter(Exception):
    pass

class TooOldToEnter(Exception):
    pass

def enter_nightclub(age):
    if age < 18: raise TooYoungToEnter("Sorry, must be 18")
    if age > 69: raise TooOldToEnter("May-be go to cafe?")
    enter()

def main():
    # .. get age again
    user_age = 77
    try:
        enter_nightclub(user_age)
    except TooYoungToEnter as e:
        print(f"Wait a bit. Info from the nightclub: {e}")
    except TooOldToEnter as e:
        print(f"Waited too long. Info from the nightclub: {e}")
    else:
        # executed if try block does not raise an exception.
        # it avoids accidentally catching an exception
        # that wasn't raised by enter_nightclub(),
        # the function for which the try-catch was meant.
        party()
