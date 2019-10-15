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

# Küsimused?

---
