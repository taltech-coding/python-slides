## Sisend-väljund
#### _input-output_

---


## Teksti väljastamine


- Kasutame funktsiooni ``print()``
- Sümboleid saab väljastada ka mujale (faili, veebi jne)
 - neid teemasid vaatame hiljem
- ``print()`` funktsiooni saab ette anda mitu argumenti
 - funktsioonidest ja argumentidest räägime järgmine kord
- Vaatame näiteid

---

## print() näited

```python
print("Hello world!")

print("Welcome")
print("to school!")

print("""Welcome
to school!""")
```

@[1](Tulemus prinditakse ühele reale, lõppu lisatakse reavahetus)
@[3-4](Iga print trükib tulemuse eraldi reale)
@[6-7](Kolmekohalise jutumärgiga saab kirjutada mitmerealist teksti, tulemus on ka mitmel real)

---

## print() näited, end="""

```python
print("Hi", end="")
print("Ago!")

print("Hi ", end="")
print("Ago!")

print("Hi", end=" ")
print("Ago!")
```
@[1-2](``end`` argumendiga saab määrata, milline on sõne lõpp. Kui seda ei määra, siis vaikimisi on lõpus reavahetus nagu eelmisel slaidil)
@[4-5](Kuna eelmise prindi tulemus läks ühele reale, aga tekstide vahel polnud tühikut,siis lisame siin eraldi tühiku esimese teksti lõppu)
@[6-7](Võime sama tulemuse [tühikuga tekst] saavutada määrates teksti lõppu tühiku)

---

## Mitme väärtuse kuvamine

```python
print("first", "second")
print(1, 2)
print("My age is", 18)
print("My age is " + str(18))
```
@[1](Komaga eraldades on võimalik mitu väärtust kuvada)
@[2](Argumendid ei pea olema sõned)
@[3](Argumentide tüübid ei ole olulised)
@[3-4](Võrdluseks arvu printimine sõnena - peame arvu [18] muutma sõneks)

---

## f-string

- Märkides sõne (teksti) ette sümboli ``f``, saab kasutada sõne sees muutujaid
 - Seda nimetatakse f-string'iks
- Kõik mis f-string'i sees loogeliste sulgude vahel on, arvutatakse Pythoni poolt välja

```python
name = "Ago"
print(f"Hi {name}!")

price_without_tax = 20
print(f"Price with tax is {price_without_tax * 1.2}")

print("Sum: {1 + 2 + 3}")
print(f"Sum: {1 + 2 + 3}")
```

@[1-2](Tulemus on "Hi Ago!")
@[4-5](Tulemus on "Price with tax is 24.0")
@[6](Tulemus on "Sum: {1 + 2 + 3}". Miks?)
@[7](Tulemus on "Sum: 6")

---

## Sisendilugemine

- Teksti lugemiseks konsoolist kasutame funktsiooni ``input()``
- See loeb sõne (teksti) kuni ``enter`` klahvi vajutamiseni
- Funktsioonile saab kaasa anda ka sõne (teksti), mis ekraanile näidatakse.

```python
name = input()
print(name)

name = input("Enter your name:")
print(f"Hi {name}!")
```

@[1-2](Küsitakse kasutaja sisendit, aga ekraanile miagi ei näidata. Kui midagi on sisestatud, kuvatakse see ekraanile)
@[3-4](Ekraanile näidatakse tekst, et kasutaja peaks sisestama nime ja oodatakse kasutaja sisendit. Kui midagi on sisestatud, kuvatakse ekraanile tervitus.)

---

## Viited

- https://ained.ttu.ee/pydoc/input.html
