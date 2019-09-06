## ITI0102 - Programmeerimise algkursus
### Sõne
#### _string_

---

## Sõne

- Sõne on objekt
- Sõne on sümbolite jada
- Sõne on muutumatu objekt (_immutable_)
 - see tähendab, et sõne ei saa muuta
 - sõne operatsioonid loovad vajadusel uue sõne ja tagastavad selle

---

## Sõne

- Sõne loomine

```python
text = "example"
text = 'example'
text = """example"""
text = '''example'''
```
---

## Mitmerealine sõne

- Mitmerealise sõne loomine

```python
text = """This
is
multline
string"""
text = '''This
too'''
text = "This \n is \n also!"

```
@[1-4](Kolmekordsete jutumärkide vahel võib kasutada reavahetust - see on osa sõnest)
@[5-6](Sama käib kolmekordsete ülakomade kohta)
@[7](``\n`` tähistab reavahetust, see sõne on kolmerealine)

---

## Sõne loomine

```python
text = "don't do it"
text = 'don\'t do it'
text = "hello ""world"    # hello world
text = "hello " + 'world'  # hello world

```

@[1](Ülakoma kasutamine "" märkide vahel on lubatud)
@[2](Ülakoma kasutamine '' märkide vahel tuleb ülakoma varjestada (_escape_))
@[3](Pythonis võib kahe sõne kokkupanemiseks need lihtsalt ükteise otsa kirjutada)
@[3-4](Sõned võib kokku liita ka + märgiga - kaks rida annavad sama tulemuse)

---

## Sõne operatsioonid

- Elementide (tähemärkide) ligipääs, lõiked (_slice_):

```python
greeting = "Hello!"
print(greeting[1])  # e

# slice [start:end], start inclusive, end exclusive
print(greeting[1:3])  # el

# slice, -1 means from end, still exclusive
print(greeting[1:-1])  # ello
```

@[1-2](Kantsulgudega saab määrata, millist elementi (sümbolit) küsime)
@[1-2](**Indeksid algavad 0-st!** St esimene täht on indeksiga 0 jne)
@[1,4-5](Lõik [algus:lõpp], algusindeks on kaasa arvatud, lõppindeks ei ole kaasa arvatud)
@[1,7-8](Kasutada saab negatiivseid indekseid, neid loendatakse tagantpoolt)

---

## Sõne lõiked

- Lõike juures saab määrata alguse, lõpu ja sammu: ``text[start:end:step]``

```python
greeting = "Hello!"

print(greeting[0:6:1])  # Hello!
print(greeting[::1])    # Hello!
print(greeting[::])     # Hello!

# every second element
print(greeting[::2])    # Hlo

# backwards
print(greeting[::-2])   # !le
```

@[1-5](Kõik annavad sama tulemuse, mõne osa lõikest võib jätta määramata)
@[1-5](Vaikimisi väärtused: 0:sõne pikkus:1)
@[1,7-8](Samm on 2, loetakse algusest lõpuni)
@[1,10-11](Samm võib olla negatiivne, liigutakse lõpust algusesse)

---

## Veel sõne operatsioone

```python
greeting = "Hello!"

print(greeting.lower())           # hello!
print(greeting.upper())           # HELLO!
print(greeting.startswith("He"))  # True
print(greeting.startswith("HE"))  # False
print(greeting.index("lo"))       # 3
print(greeting.count("l"))        # 2
print(greeting.replace("e", "a"))  # Hallo!
```

---

## Viiteid

- https://ained.ttu.ee/pydoc/string.html
- https://docs.python.org/3/library/string.html
