def enter():
    pass

def party():
    pass

def enter_nightclub(age):
    if age < 18:
        raise ValueError("Too young")
    if age > 69:
        raise ValueError("Too old")
    enter()

def main():
    # get user age
    age = 19
    try:
        enter_nightclub(age)
        party()
    except ValueError as e:
        print(f"Sorry, no party for you. Reason: {e}.")