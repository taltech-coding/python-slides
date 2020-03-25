a = dict(one=1, two=2, three=3)
b = dict([('two', 2), ('three', 3), ('one', 1)])
d = {'three': 3, 'one': 1, 'two': 2}
print(a == b == d)  # True

count = len(d)  # => 3

print(d['one'])  # => 1
d['one'] = 5  # value for key 'one' will become 5


