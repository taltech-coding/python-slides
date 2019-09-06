text = "example"
text = 'example'
text = """example"""
text = '''example'''

text = "don't do it"
text = 'don\'t do it'
text = "hello" '"world'""

text = "hello " + 'world'
text = "hello ""world"
print(text)

text = """This
is
multline
string"""
text = '''This
too'''
text = "This \n is \n also!"
print(text)

# ----

greeting = "Hello!"
print(greeting[1])  # e

# slice [start:end], start inclusive, end exclusive
print(greeting[1:3])  # el

# slice, -1 means from end, still exclusive
print(greeting[1:-1])  # ello

# ---

greeting = "Hello!"

print(greeting[0:6:1])  # Hello!
print(greeting[::1])    # Hello!
print(greeting[::])    # Hello!

# every second element
print(greeting[::2])    # Hlo

# backwards
print(greeting[::-2])   # !le

## ----

greeting = "Hello!"

print(greeting.lower())           # hello!
print(greeting.upper())           # HELLO!
print(greeting.startswith("He"))  # True
print(greeting.startswith("HE"))  # False
print(greeting.index("lo"))       # 3
print(greeting.count("l"))        # 2
print(greeting.replace("e", "a"))  # Hallo!