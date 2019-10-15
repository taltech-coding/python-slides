import math

def calculate_square_root(value):
    try:
        sqrt = math.sqrt(value)
        return sqrt
    except (ValueError, ZeroDivisionError) as e:
        print(f"Got value or /0 error {e}")
        return -1
    except TypeError as e:
        print(f"Got type error {e}")
        return -2
    except Exception as e:
        print(f"Some other error {e}")
        return -10