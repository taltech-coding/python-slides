## Tingimuslause
#### if statement

---

## Tingimuslause

- Tavapäraselt toimub koodi täitmine järjest ridade haaval
- Mõne osa koodist tahaks käivitada vaid teatud tingimusel
- Näiteks: kui piim on otsa saanud, telli uus piim;
- Või: Kui Marsi pind läheneb, muuda lennurežiim maandumise peale
- Selleks kasutame tingimuslauset ``if``

---

## Tingimuslause näide

```python
print("start")
if 4 > 2:
    print("sometimes run me")
print("end")

```

@[1](See rida täidetakse alati)
@[2-3](See osa trükitakse välja vaid juhul, kui tingimus on tõene (antud juhul 4 on alati suurem kui 2, seega käivitatakse sisemine osa))
@[3](Oluline on jälgida, et tingimuslause käivitatava osa ees on taane 4 tühikut)
@[4](See rida täidetakse alati)

---

## Tingimuslause näide miterealine

```python
a = 4
print("start")
if a > 2:
    print("sometimes run me")
    print("Then run me too!")
print("end")
```

@[4-5](Siin täidetakse mitu korraldust - kõik, mis on taandega if-lause all)

---

## Tingimuslause mitu valikut

```python
a = 5
b = 7
if a < b:
    print(str(a) + " on väiksem kui " + str(b))
elif a > b:
    print(str(a) + " on suurem kui " + str(b))
else:
    print(str(a) + " ja " + str(b) + " on võrdsed!")
```

@[5-6](``elif`` kontrollitakse vaid juhul, kui eelmised tingimused ei ole tõesed)
@[7-8](``else` osa täidetakse juhul, kui ükski eelmine tingimus ei olnud tõene)

---

## Tingimuslause

- Tingimuslause võimaldab mingit osa koodi käivitada vaid teatud juhul
- Tingimuslausesse tuleb kirjutada kontroll, mis saab olla kas tõene või väär
- Tingimuslause võib koosneda mitmest harust
 - esimene haru on alati ``if`` koos tingimusega
 - sellele võib järgenda mitu ``elif`` osa koos tingimusega
 - lõpus võib olla ``else`` osa ilma tingimuste
- **Alati täidetakse vaid üks haru**

---

## Tingimuslause ja taanded

```python
a = 5
b = 2
if a > 4:
    if b > 1:
        print("on nii")
    print("ja ei ole")
```

Mis on väljund?

@ul
- on nii
- ja ei ole
@ulend

---

## Tingimuslause ja taanded

```python
a = 5
b = 1
if a > 4:
    if b > 1:
        print("on nii")
    print("ja ei ole")
```

Mis on väljund?

@ul
- ja ei ole
@ulend

---

## Viited

- https://ained.ttu.ee/pydoc/if_statements.html
- https://docs.python.org/3/tutorial/controlflow.html#if-statements