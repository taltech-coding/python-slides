## Sõnastik
#### _dictionary_

---

## Sõnastik (_dict_)

- Järjendi (_list_) elemendid on järjestikuste arvudega positsioonidel (0, 1, 2, ..)
- Sõnastikus (_dict_) saab kasutada võtmena suvalisi arve ja sõnesid

 - Täpsemalt kõiki muutumatuid (_immutable_) andmetüüpe
 
- Kasutatakse vastavuste loomiseks

---

## Sõnastik (_dict_)

- Loomine

```python
a = dict(one=1, two=2, three=3)
b = dict([('two', 2), ('three', 3), ('one', 1)])
d = {'three': 3, 'one': 1, 'two': 2}

print(a == b == d)  # True
```

- Elementide kogus

```python
count = len(d)  # => 3
```

- d[key] - konkreetse elemendi poole pöördumine

```python
print(d['one'])  # => 1
d['one'] = 5  # value for key 'one' will become 5
```