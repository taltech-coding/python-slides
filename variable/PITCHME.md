## Muutuja
#### *variable*

---

## Muutuja

- Kokkupuude matemaatikas ("Leia *x*")
- Programmeerimises on muutuja nimega viide "väärtusele"
- Pythonis muutujal ei ole andmetüüpi (mõnes keeles on)
- "Väärtusel" aga on andmetüüp

```python
age = 18
name = "Student"
```

---

## Muutuja kasutamine

```python
greeting = "Hello all!"
student_count = 300

print(greeting)
print("Students:", student_count)

greeting = "Hi"                     # value is changed
student_count = student_count + 2   # add 2

print(greeting)
print("Students:", student_count)

greeting += " students!"            # same as greeting = greeting + " .. "
print(greeting)
```

@[1](Loome muutuja ``greeting`` ja anname sellele tekstilise väärtuse [sõne])
@[2](Loome muutuja ``student_count`` ja anname sellele täisarvulise väärtuse)
@[4](Prindime tervituse)
@[5](Prindime tudengite arvu)
@[7](Muudame tervituse väärtust)
@[8](Suurendame tudengite arvu kahe võrra)
@[10](Prindime uue tervituse)
@[11](Prindime uue tudengite arvu)
@[13](Lisame tervitusele natuke teksti. `a += 1` saab kasutada `a = a + 1` asemel.)
@[14](Prindime uuendatud tervituse)


---

## Muutuja nimetamine

@ul
- Pythonis kasutame väikeseid tähti
- Mitmesõnalised muutujad eraldatakse allkriipsuga (_)
- Pigem kasutada mõtestatud nimetusi (``age``), mitte lühendeid/suvalisi tähistusi (``a``).
- @color[green](Head näited): `temperature`, `student_count`
- @color[red](Halvad näited): `a`, `temp`, `VAL`, `SomeValue` jne.
@ulend

---

## Muutuja Pythonis

@ul
- Pythonis on iga "asi" objekt, st iga väärtus on objekt
- Muutuja on nimi, mis viitab mingile objektile
- Objektidest räägime aga hiljem (u 11. nädal)
@ulend

---

## Veel näiteid

```python
border_size = 10
border_size = border_size + 2
picture_height, picture_width = 100, 200
whole_frame_height = border_size + picture_height + border_size
whole_frame_width = picture_width + 2 * border_size
picture_height, picture_width = picture_width, picture_height

```

@[1-2](Määrame uue väärtuse, kasutades vana väärtust. Mis on uus väärtus?)
@[3](Pyhonis saab määrata mitmele muutujale väärtuse korraga)
@[4-5](Arvutame pildi + raami suurused. Muutujad asendatakse väärtustega arvutamise hetkeks)
@[6](Siin vahetatakse muutujate väärtused)

---

## Muutujal andmetüüpi pole

```python
meaningful_variable = 10
print(meaningful_variable)  # 10
print(type(meaningful_variable))  # <class 'int'>

meaningful_variable = "hello"
print(meaningful_variable)  # hello
print(type(meaningful_variable))  # <class 'str'>

meaningful_variable = 9 / 2
print(meaningful_variable)  # 4.5
print(type(meaningful_variable))  # <class 'float'>

```

@[1-3](Muutujale omistatakse täisarv, tüüp on klass ``int``)
@[5-7](Samale muutujale omistame sõne ehk teksti, tüüp on klass ``str``)
@[9-11](Muutujale omistatakse jagatise tulemus, mis on ujukomaarv, tüüp on klass ``float``)

---

## Väärtusel on andmetüüp

```python
string_value = "redis"
int_value = 13

redis_13 = string_value + int_value  # ERROR!
redis_13_str = string_value + str(int_value)
redis_15 = redis_13 + 2

``` 
@[1-2](Loome ühe sõne ja ühe täisarvu)
@[4](Sõne ja arvu ei saa kokku liita)
@[5](Saame vajaliku tulemuse, kui "muudame" ``int_value`` sõneks, seejärel liidetakse kaks sõne)
@[6](Arve saab kokku liita. ``redis_13`` asendatakse arvutamise hetkeks vastava väärtusega)

---

## Muutuja

@ul
- Muutuja on nimetus, "pesa", kuhu pannakse mingi väärtus.
- Muutuja abil saab väärtust lugeda ja (üldiselt ka) muuta.
- Muutujal (ehk nimel) ei ole andmetüüpi. Samasse muutujasse saab alguses kirjutada arvu, seejärel sõne.
- Väärtus (millele muutuja viitab) on andmetüüp.
@ulend

---

## Viited

- https://ained.ttu.ee/pydoc/variable.html
