## ITI0102 - Programmeerimise algkursus
### Järjend, ennik, hulk
#### _list_, _tuple_, _set_

---

## Järjend (_list_)

- Kasutatakse loetelu esitamiseks
- Järjendiga realiseeritakse järjekordi (_queue_) ja pinusid (_stack_)
- Järjendi elemendid on kindlas järjekorras

```python
empty_list = []

scientists = ["Turing", "Dijkstra", "Knuth", "Kolmogorov"]

```

---

## Operatsioonid järjendiga

```python
print(scientists)        # ['Turing', 'Dijkstra', 'Knuth', 'Kolmogorov']
print(len(scientists))   # -> 4
if "Dijkstra" in scientists:
    print("Dijkstra is a scientist!")  # -> Dijkstra is a scientist
```

@[1](Järjendi kuvamine)
@[2](Järjendi elementide arv (pikkus))
@[3-4](Kuulumise kontroll, kas "Dijkstra" on järjendis)

---

## Operatsioonid järjendiga

- Järjendi ühe elemendi või lõigu (_slice_) kuvamine

```python
print(scientists[0])    # -> Turing
print(scientists[0:2])  # -> ['Turing', 'Dijkstra']
``` 

@[1](Kantsulgude vahel arv tähistab indeksit; esimese elemendi indeks on 0)
@[2](Alamlisti ehk kõigu jaoks määrame ära algus- ja lõpuindeksi; lõpuindeks ei ole kaasa arvatud)

---

## Operatsioonid järjendiga

- Minimaalse ja maksimaalse elemendi leidmine
- Summa leidmine

```python
print(min([42, 12, 99, 61]))   # -> 12
print(max([42, 12, 99, 61]))   # -> 99
print(sum([42, 12, 99, 61]))   # -> 214

```

---

## Elementide lisamine

```python
numbers = [1, 2]
numbers.append(3)           # add in the end
print(numbers)              # -> [1, 2, 3]

numbers.insert(1, 4)        # insert into middle
print(numbers)              # -> [1, 4, 2, 3]

numbers = numbers + [5, 6]  # add another list into end
print(numbers)              # -> [1, 4, 2, 3, 5, 6]
```

---

## Elementide eemaldamine

```python
numbers = [2, 4, 6, 4]
numbers.remove(4)     # remove first by value
print(numbers)        # -> [2, 6, 4]

numbers = [2, 4, 6, 4]
numbers.pop(2)        # remove by index
print(numbers)        # -> [2, 4, 4]
```

---

## Tsükkel

```python
numbers = [2, 4, 6]
for index in range(len(numbers)):
    print(f"Element at {index} has value {numbers[index]}")

for element in numbers:
    print(element)

for index, element in enumerate(numbers):
    print(f"Element at {index} has value {numbers[index]}")
```

@[1-3](Kasutame ``range``'i, et saada indeksid 0 kuni järjendi pikkus - 1)
@[1,5-6](``for`` tsükkel vaikimisi käibki läbi kõik elemendid, mis on etteantud järjendis)
@[1,8-9](``enumerate`` tagastab lisaks elemendile ka indeksi - saab kätte nii indeksi kui väärtuse korraga)

---

## Mitmemõõtmeline järjend

```python
people_groups = [
    ["Ago", "Mati"],
    ["Kati", "Kiur"],
    ["Malle", "Diana", "Saldur"]
]

print(people_groups[0][0])    # Ago
print(people_groups[2][1])    # Diana
print(len(people_groups[1]))  # 2
print(len(people_groups[2]))  # 3
```

---

## Mitmemõõtmeline järjend

- Mõlemad näited annavad sama tulemuse

```python
for group_idx in range(len(people_groups)):
    for name in people_groups[group_idx]:
        print(name, end=", ")

for group in people_groups:
    for name in group:
        print(name, end=", ")
```

---

## Ennik (_tuple_)

- Ennik on muutumatu järjend
 - elemente ei saa muuta
 - elemente ei saa lisada
 
```python
t = ()
t = (1, )   # NB! not t = (1)
t = (1, 2, 3, 4)

print(t[0])    # 1
print(t[0:2])  # (1, 2), slice returns a new list
```
---

## Hulk (_set_)

- Hulgas pole korduvaid elemente
- Hulga elemendid ei ole järjestatud
- Hulgast ei saa indeksiga elemente küsida

```python

names = {"ago", "kati"}
print(names)    # {"ago", "kati"}

for name in names:
    print(name)

names.add("rasmus")  # "rasmus" will be added
names.add("ago")     # "ago" is not added, duplicate
print(names)         # {'rasmus', 'kati', 'ago'}
```

---

## Viited

- https://ained.ttu.ee/pydoc/list.html
- https://ained.ttu.ee/pydoc/tuple.html
- https://ained.ttu.ee/pydoc/set.html