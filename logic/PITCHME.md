## Loogika
### _logic_

---

## Loogilised väärtused

- _boolean_ tüüpi väärtuseid on kaks:
- ``True`` - tõene
- ``False`` - väär

```python
i_am_smart = True
i_like_to_wake_up_early = False
```

---

## võrdlus

- Võrdlus annab tulemused loogika väärtuse

```python
some_number = 111111
is_big_number = some_number > 1000        # True
is_small_number = some_number < 10        # False
is_correct_number = somenumber == 111111  # True
between = 123 < some_number < 222222      # True
```

---

## Loogika avaldised

- Saab kasutada operatsioone ``and`` ja ``or``

```python
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # True

print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False
```

---

## Grupeerimine

- Järjekorra ja grupeerimise jaoks saab kasutada sulge

```python
is_monday = True
is_sunny = False
is_warm = True
print(is_monday or is_warm and is_sunny)   # True
print( (is_monday or is_warm) and is_sunny)  # False
```

@[1-4](``and`` on prioriteetsem kui ``or``)
@[1-4,5](Siin sulgudes olev avaldis arvutatakse enne, seejärel toimub ``and``)
