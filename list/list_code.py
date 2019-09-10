empty_list = []

scientists = ["Turing", "Dijkstra", "Knuth", "Kolmogorov"]


print(scientists)        # ['Turing', 'Dijkstra', 'Knuth', 'Kolmogorov']
print(len(scientists))   # -> 4
if "Dijkstra" in scientists:
    print("Dijkstra is a scientist!")  # -> Dijkstra is a scientist


print(scientists[0])    # -> Turing
print(scientists[0:2])  # -> ['Turing', 'Dijkstra']


print(min([42, 12, 99, 61]))   # -> 12
print(max([42, 12, 99, 61]))   # -> 99
print(sum([42, 12, 99, 61]))   # -> 214

numbers = [1, 2]
numbers.append(3)           # add in the end
print(numbers)              # -> [1, 2, 3]
numbers.insert(1, 4)        # insert into middle
print(numbers)              # -> [1, 4, 2, 3]
numbers = numbers + [5, 6]  # add another list into end
print(numbers)              # -> [1, 4, 2, 3, 5, 6]


numbers = [2, 4, 6, 4]
numbers.remove(4)     # remove first by value
print(numbers)        # -> [2, 6, 4]

numbers = [2, 4, 6, 4]
numbers.pop(2)        # remove by index
print(numbers)        # -> [2, 4, 4]

numbers = [2, 4, 6]
for index in range(len(numbers)):
    print(f"Element at {index} has value {numbers[index]}")

numbers = [2, 4, 6]
for element in numbers:
    print(element)

numbers = [2, 4, 6]
for index, element in enumerate(numbers):
    print(f"Element at {index} has value {numbers[index]}")


people_groups = [
    ["Ago", "Mati"],
    ["Kati", "Kiur"],
    ["Malle", "Diana", "Saldur"]
]

print(people_groups[0][0])    # Ago
print(people_groups[2][1])    # Diana
print(len(people_groups[1]))  # 2
print(len(people_groups[2]))  # 3

for group_idx in range(len(people_groups)):
    for name in people_groups[group_idx]:
        print(name, end=", ")

for group in people_groups:
    for name in group:
        print(name, end=", ")


t = ()
t = (1, )   # NB! not t = (1)
t = (1, 2, 3, 4)

print(t[0])    # 1
print(t[0:2])  # (1, 2), slice returns a new list

# set

names = {"ago", "kati"}
print(names)    # {"ago", "kati"}

for name in names:
    print(name)

names.add("rasmus")  # "rasmus" will be added
names.add("ago")     # "ago" is not added, duplicate
print(names)         # {'rasmus', 'kati', 'ago'}