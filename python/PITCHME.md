## Python

---

## Ajalugu

- Nimi pärineb “Monty Pythoni lendav tsirkus” sketšisarjast
- Esimene versioon aastast 1991
- Autor on Guido van Rossum
- 2018 juulis astus tehnilise juhi kohalt tagasi
- Peamised programmeerimiskeelelised põhimõtted pärinevad keelest ABC
- TIOBE indeksi järgi 4. koht (peale Java, C, C++), 7%
- StackOverflow survey järgi 4. koht (peale JavaScript, Java, Bash), 40%

---

## Python

- Viimane versioon 3.7
- Python on tüüpiliselt interpreteeritav keel
 - programmikood käivitatakse jooksvalt
 - võrdluseks kompileeritav keel - lähtekood kompileeritakse masinkoodiks 
   ning seejärel käivitatakse näiteks baitkood.
- Kood on üldiselt lihtsasti loetav
- Töötab erinevate operatsioonisüsteemide peal
- Väga palju tööriistu on realiseeritud Pythonis

---

## Programmikood

- Pythonit võib jooksutada interaktiivselt
 - abiks näiteks kalkulaatorina kasutamisel
- Üldiselt kirjutame faili (lähtekood), mida käivitame
- Pythoni faili laiend on `.py`, näiteks `hello.py`
- Käivitamisel loetakse seda faili ridahaaval
- Vigadest antakse teada nende tekkimisel

---

## hello world

```python
# This program prints out "Hello world!"

print("Hello world!")
```

@[1](Kommentaar, # märgist kuni rea lõpuni ignoreeritakse)
@[3](Kirjutab teksti ekraanile)

---

## hello world

- Eelnev kood salvestada näiteks faili ` hello.py`
- Käivitamisel ilmub ekraanile tekst ` Hello world!`

```text
Hello world!
```

---

### Käivitamine

- Käsureal `python3 hello.py`

![Execution](python/execution.png)

---

## Näide

```python
print("Hello, I am your program!")
name = input("What is your name: ")
print(f"Hello {name}!")
```
---

## Viited

- https://docs.python.org/3/ Pythoni ametlik dokumentatsioon
- https://ained.ttu.ee/pydoc/ Kursuse "ametlik" materjal
