## ITI0102 - Programmeerimise algkursus
### Andmestruktuurid
#### _data structures_
##### Ago Luberg

---

## Andmestruktuurid

- Sõne (_string_)
- Järjend (_list_)
- Ennik (_tuple_)
- Hulk (_set_)
- Sõnastik (_dictionary_)

---

## Sõne

- Muutumatu
- Sõne "muutmine" (sõne liitmine, `replace()`, `remove()` jne) loovad uue sõne
- Vajalik kasutada, kui andmetüüp peab olema sõne
- Loomine: `s = "Hello"`
- Tsükkel: `for char in s:`

---

## Järjend

- Järjestatud elementide andmekogu
- Elemente saab lugeda ja muuta indeksi kaudu: `mylist[2] = 1`
- Indeksid täisarvud alates 0-st
- Vajalik, kui järjekord on oluline
- Loomine: `mylist = [1, 2, 3]`
- Tsükkel: `for element in mylist:`

---

## Ennik

- Muutumatu järjestatud elementide andmekogu
- Elemente saab lugeda indeksi kaudu, indeks algab 0-st
- Vajalik, kui andmeid ei tohi muuta
- Loomine: `mytuple = (1, 2, 3)`
- Tsükkel: `for element in mytuple:`

---

## Hulk

- Unikaalsete elementide kogu
- Ei säilita järjekorda
- Elemente ei saa küsida indeksi järgi
- Kasutadakse, kui duplikaate pole vaja
- Loomine: `myset = set()`
- Tsükkel: `for element in myset:`

---

## Sõnastik

- Võti-väärtus paarid
- Üldiselt ei hoia järjekorda (Python 3.6-st alates hoiab)
- Kasutatakse seoste loomiseks
- Võtmed on unikaalsed, seega võtmed moodustavad justkui hulga (_set_)
- Võtmed võivad olla muutumatud objektid (arv, sõne, ennik)
- Loomine: `mydict = {}`
- Tsükkel üle võtmete: `for key in mydict:`

---

## Keerukus, efektiivsus

- Erinevad andmestruktuurid on erineva keerukusega
- Näiteks elemendi leidmine hulgas `x in data`
  - järjend: vaadatakse kõik elemendid läbi
  - hulk: vaadatakse ühte elementi vaid
  - sõnastik (võtme otsing): vaadatakse ühte elementi 
- https://wiki.python.org/moin/TimeComplexity

---

# Küsimused?

---
