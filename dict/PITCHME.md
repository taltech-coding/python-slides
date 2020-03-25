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

---

## Sõnastik (_dict_)

- key in d - kas selline võti on olemas
```python
print('one' in d) # => True
print('zero' in d) # => False
print(1 in d) # => False
```
- keys() - tagastab võtmete nimekirja
```python
print(d.keys()) # => dict_keys(['three', 'one', 'two'])
print(type(d.keys())) # => <class 'dict_keys'>
```
- values() - tagastab väärtuste nimekirja
```python
print(d.values()) # => dict_values([3, 5, 2])
print(type(d.values())) # => <class 'dict_values'>
```
- items() - tagastab (võti, väärtus) paaride nimekirja
```python
print(d.items()) # => dict_items([('three', 3), ('one', 5), ('two', 2)])
print(type(d.items())) # => <class 'dict_items'>
```
---

## Sõnastik (_dict_)

- Järjekord ei ole oluline
```python
a = {'three': 3, 'two': 2, 'one': 1}
c = {'two': 2, 'three': 3, 'one': 1}
d = {'one': 1, 'two': 2, 'three': 3}
print(a == b == d) # True
```
- Võtme andmetüüp on oluline
```python
a = {'1': 1, '2': 2}
a[1] = 11
a[2] = 22
print(a) # => {'1': 1, '2': 2, 1: 11, 2: 22}
```
---

## Sõnastik (_dict_)

- Väärtus võib omakorda sõnastik olla
```python
training = {
'monday': {'10:00': 'run', '12:00': 'swim'},
'wednesday': {'18:00': 'gym', 'late': 'walk'},
'friday': {'morning': 'yoga'}}
print(training['friday']['morning']) # => yoga
training['thursday'] = {'night': 'powersleep'}
```
- Sama võtmega saab olla vaid üks väärtus
```python
d['one'] = 1
d['one'] = 2
print(d['one']) # => 2
```

---