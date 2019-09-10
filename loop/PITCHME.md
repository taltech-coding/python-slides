## ITI0102 - Programmeerimise algkursus
### Tsükkel
#### _loop_

---

## Tsükkel (_loop_)

- Tsükkel võimaldab koodiplokki täita mitu korda
- Tavaliselt on tsükkel lõplik (täidetakse määratud arv kordi)
 - on võimalik kirjutada ka "lõputut" tsüklit
 - kuigi ka siis lõpetatakse "lõputu" tsükkel teatud tingimusel ära
 
---

## ``for`` tsükkel

- Võtab järjest elemente etteantud järjendist/hulgast
- Kõige tavalisem tsükkel kasutab funktsioon ``range()``
 - ``range(n)`` genereerib täisarve vahemikus ``[0, n)`` (0 on kaasa arvatud, n ei ole)
 
```python
for i in range(10):
    print(i)
```

---

## ``for`` tsükkel

- ``range()`` funktsioonile saab määrata ka alguse:
 - ``range(start, end)`` annab täisarvud vahemikus ``[start, end)``
 - ``start`` on kaasa arvatud, ``end`` ei ole kaasa arvatud
 
```python
for i in range(4, 7):
    print(i)
```

---

## ``for`` tsükkel

- ``range()`` funktsioonile saab määrata ka sammu:
 - ``range(start, end, step)`` annab täisarvud vahemikus ``[start, end)`` nii, et kahe järjestikuse arvu vahe on ``step``.

```python
for i in range(1, 10, 3):
    print(i)
```

---

## ``while`` tsükkel

- ``while`` tsükliga korratakse koodiosa seni, kuni tingimus on tõene
 - tingimus on nagu ``if`` lauses
 
```python
i = 0
while i < 10:
    print(i)
    i = i + 1

```

---

## ``break``, ``continue``

- Tsükli sees on võimalik kasutada:
- ``break`` - lõpetab tsükli täitmise
- ``continue`` - jätkab tsükli täitmist alugsest
 - ``for`` tsükli puhul võtab järgmise elemendi
 - ``while`` tsükli puhul kontrollib tingimust
 
```python
i = 0
while True:
    i += 1
    if i % 3 == 0:
        continue
    if i > 10:
        break
    print(i)
```

---

## Viited

- https://ained.ttu.ee/pydoc/loop.html
- https://docs.python.org/3/tutorial/controlflow.html#for-statements