## ITI0102 - Programmeerimise algkursus
### Erind
#### _Exception_
##### Ago Luberg

---


## Erind (_exception_)

- Erind on programmi töö käigus tekkiv ootamatu olukord (näiteks viga)

- Programmikood on süntaktiliselt korrektne, aga programmi käivitamisel tekib töö käigus viga

---

## Erind

- Paljud erindid ei ole programmi töö jaoks tingimata fataalsed (_unconditionally fatal_)
- Teatud juhtudel saab programmi tööd jätkata, kui eriolukord suudetakse lahendada
- Paljusid erindeid saab töödelda ja seda tegevust nimetatakse erinditöötluseks (_execption handling_)

---

## Erind

```python
import math

def calculate_square_root(value):
    return math.sqrt(value)

# ... ask for user input
# user enters -1
user_input = -1

calculate_square_root(user_input)
```

---

## Erind (tulemus)

```text
Traceback (most recent call last):
 File "exception_code.py", line 10, in <module>
  calculate_square_root(user_input)
 File "exception_code.py", line 4, in calculate_square_root
  return math.sqrt(value)
ValueError: math domain error
```

@[1](`traceback` - kuvatakse kõik programmi jooksul toimunud väljakutse vea tekke hetkel.)
@[2-3](Antud juhul failis `exception_code.py` real 10 tekkis viga)
@[4-5](`calculate_square_root` funktsiooni väljakutses real 4 tekkis viga)
@[5-6](`math.sqrt` funktsioonis tekkis viga `ValueError`.)

---

## Erindi vältimine

- Proovime selliseid olukordi vältida kasutades tingimuslauseid

```python
import math

def calculate_square_root(value):
    if value < 0:
        print("Must not be a negative number")
        return -1  # return something to understand something went wrong
    return math.sqrt(value)

# ... ask for user input
# user enters -1
user_input = -1

calculate_square_root(user_input)
```
@[4-6](Lisame tingimuslause. Midagi peame tagastama ka, aga mida?)

- Prindib `Must not be a negative number`

---

## Erind

- Kasutaja sisestab nüüd `a`

```text
Traceback (most recent call last):
File "exception_str.py", line 13, in <module>
  calculate_square_root(user_input)
File "exception_str.py", line 4, in calculate_square_root
  if value < 0:
TypeError: '<' not supported between instances of 'str' and 'int'
```
---

## Erinditöötlus (_exception handling_)

- Tekkivad erindid saab kinni püüda (_catch_)
- Selleks kasutatakse `try ... except` konstruktsiooni
- Kui selles vahemikus tekib erind, on see võimalik kinni püüda
- `try ... except` plokis jääb koodi täitmine pooleli sealt realt, kus viga tekib
- Kinnipüüdmise korral on võimalik midagi ette võtta, et programmi töö saaks jätkuda

---

## Erinditöötlus (_exception handling_)

```python
try:
    sqrt = math.sqrt(-1)
    print(sqrt)
except:
    print("An exception was raised")
```
@[1-4](Kui siin plokis tekib erind, püütakse see kinni. `print` käsku sellisel juhul ei täideta.)
@[4-5](Kui `try` plokis tekkis viga, püütakse see siin kinni ja täidetakse. Kui viga ei teki, siis seda koodi ei käivitata)

---

## Erindi tüüp

- `except` plokis on võimalik ainult teatud tüüpi vigu püüda
- `try` plokile võib järgneda 1 või mitu `except` plokki

  - käivitatakse vaid esimene, mis sobib
  
- Üks `except` võib püüda ka mitut tüüpi erindit
  - Tüübina läheb arvesse ka alamtüüp (alamklasls)
 
---

## Erindi tüüp

```python
import math

def calculate_square_root(value):
    try:
        sqrt = math.sqrt(value)
        return sqrt
    except (ValueError, ZeroDivisionError) as e:
        print(f"Got value or /0 error {e}")
        return -1
    except TypeError as e:
        print(f"Got type error {e}")
        return -2
    except Exception as e:
        print(f"Some other error {e}")
        return -10
```

@[7-9](Kuigi nulliga jagamise viga näites ei teki, on see näide, kuidas mitut erindit ühe plokiga püüda.)
@[7-15](`except ExceptionName as e` võimaldab plokis kasutada muutujat `e`, et saada lisainfot erindi kohta.)

---

## Erindi tõstmine

- Programm võib vajadusel tõsta (_raise_) erindi
- See tähendab, et programm ise tekitab "vea"
- Üldiselt kasutatakse funktsioonides
- Funktsiooni väljakutsuja saab ise otsustada, kuidas mingi vea puhul käituda
- Näiteks ebakorrektse sisendi korral võib funktsioon tagastada -1
- Samas funktsiooni väljakutsuja ei tea, mis viga täpselt tekkis

---

## Erindi tõstmine

- Erindit saab tõsta käsuga `raise`
- Sellele järgneb erindi objekt, millel on üldiselt üks kohustuslik argument: teade (_message_)
- Kui nüüd keegi kutsub välja funktsiooni, saab ta ise otsustada, kuidas käituda "vea" puhul

---

## Erindi tõstmine

```python
def enter_nightclub(age):
    if age < 18:
        raise ValueError("Too young")
    if age > 69:
        raise ValueError("Too old")
    enter()
```
@[2-3](Kui vanus on alla 18, tõstetakse erind. Funktsiooni töö lõppeb.)

---

## Erindi tõstmine

```python
def enter_nightclub(age):
    if age < 18:
        raise ValueError("Too young")
    if age > 69:
        raise ValueError("Too old")
    enter()
    
def main():
    # get user age
    age = 19
    try:
        enter_nightclub(age)
        party()
    except ValueError as e:
        print(f"Sorry, no party for you. Reason: {e}.")
```

---

## Oma erindi defineerimine

- Programm võib kirjeldada uue erinditüübi
- Erind on objekt, seega uue erinditüübi defineerimiseks laiendame mõnda olemasolevat
- Üldiselt piisab tüübi defineerimisest, mingit täiendavat sisu (laiendust) vaja pole

```python
class RobotInvalidInputException(Exception):
    pass
```

---
## Erindi näide

```python
class TooYoungToEnter(Exception):
    pass
    
class TooOldToEnter(Exception):
    pass

def enter_nightclub(age):
    if age < 18: raise TooYoungToEnter("Sorry, must be 18")
    if age > 69: raise TooOldToEnter("May-be go to cafe?")
    enter()
    
def main():
    # .. get age again
    user_age = 77
    try:
        enter_nightclub(user_age)
    except TooYoungToEnter as e:
        print(f"Wait a bit. Info from the nightclub: {e}")
    except TooOldToEnter as e:
        print(f"Waited too long. Info from the nightclub: {e}")
    else:
        # executed if try block does not raise an exception.
        # it avoids accidentally catching an exception
        # that wasn't raised by enter_nightclub(),
        # the function for which the try-catch was meant.
        party()
```

---

# Küsimused?

---
