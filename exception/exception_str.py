import math

def calculate_square_root(value):
    if value < 0:
        print("Must not be a negative number")
        return -1  # return something to understand something went wrong
    return math.sqrt(value)

# ... ask for user input
# user enters -1
user_input = 'a'

calculate_square_root(user_input)