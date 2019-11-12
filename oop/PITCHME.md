## ITI0102 - Programmeerimise algkursus
### Objektid, klassid
#### _objects_, _classes_, OOP

---

## Objekt

@ul
- Objekt kirjeldab ära konkreetse loogilise kogumi
  - näiteks õues olev punane auto on üks objekt
  - selle taga olev roheline auto on teine objekt jne
- Tavaliselt mõtleme me arvust kui ühest väärtusest (nt 7)
- Objekt koosneb tavaliselt mitmest väärtusest
  - värv, mark, mudel, pikkus, registrimass jne
@ulend

---

## Klass

@ul
- Klass kirjeldab ära struktuuri
  - näiteks autol on värv, pikkus jne
- Klass (üldiselt) ei sisalda andmeid
- Klass on andmetüüp
- Samatüüpi andmed pärinevad kõik ühest klassist
  - punane auto on auto, roheline auto on auto jne
- Kuigi meil on maailmas mitu autot (objekti), siis meil on üks klass auto
@ulend

---

## OOP

@ul
- Objekt-orienteeritud programmeerimine (OOP) on programmeerimise paradigma, mis kasutab objekte

- Python on objekti-orienteeritud programmeerimiskeel (OOP)

- Pythonis kõik asjad on objektid
@ulend

---

## OOP tehnikad

@ul
- Kapseldamine (_encapsulation_)
  - funktsionaalsus peidetakse
- Modulaarsus (_modularity_)
  - programm jagatakse iseseisvateks tükkideks
- Polümorfism (_polymorphism_)
  - alamklass saab meetodeid üle kirjutada
- Pärimine (_inheritance_)
  - alamklass pärib omadused ja meetodid
@ulend

---

## Sõne

@ul
- Sõne on objekt
- Kui loote uue sõne, siis tegelikult luuakse uus objekt, mille tüüp on `str`.
- Sõne "funktsioone" kutsutakse meetoditeks
  - ehk siis klassis kirjeldatud funktsioonid on meetodid
@ulend

---

## Sõne
 
```python zoom-15
s = "Hello"
print(type(s))  # <class 'str'>
print(id(s))  # 30773472
print(id(s.replace("H", "h")))  # 61507648

```

@[1-2](Loome sõne `s` ja küsime selle tüübi. Tüüp on `str` klass)
@[1-3](`id` tagastab objekti kohta unikaalse arvu. Kui id on erinev, siis on ka objekt erinev (st mälus erinevas kohas))
@[1-4](`replace` teeb uue sõne, seda näeme ka `id`-ga)
@[4](`replace` on sõne meetod ehk funktsioon, mida saab välja kutsuda objektil)

---

## List

```python zoom-12
a = [1, 2, 3]
b = [1, 2, 3]
c = b

print(id(a))   # 44058024
a.append(4)
print(id(a))   # 44058024 still the same
print(id(b))   # 44059184
print(id(c))   # 44059184 - same as b
b.pop()
print(id(b))   # 44059184 - still the same
print(id(c))   # 44059184 - and same
```
@[1-3](Loome kolm listi)
@[1-7](List on _mutable_, seega elemendi lisamine muudab olemasolevat listi. `id` jääb samaks)
@[1-3,8,9](`b=c` puhul viitavad mõlemad samale objektile)
@[1-3,8-12](Ühe listi muutmine muudab mõlemat)

---

## Veel objekte

```python zoom-15
print(type(1))     # <class 'int'>
print(type(True))  # <class 'bool'>
print(type(1.2))   # <class 'float'>
print(type(None))  # <class 'NoneType'>
print(type(len))   # <class 'builtin_function_or_method'>
print(type(type))  # <class 'type'>
```

---

## Klass kui andmetüüp

@ul
- Iga klass on andmetüüp
- Näiteks on Pythonis klass `str`
- Iga konkreetne sõne, näiteks `"tere"`, on selle klassi objekt (ehk isend)
- Ühest klassist saab luua lõpmata palju objekte
- Objekti kohta öeldakse ka isend ja instants
  - Üldiselt mõeldakse "objekt", "isend", "instants" terminitega samu asju
  - Erinevates allikates võivad neil erinevused olla
  - Siin aines kasutame termineid objekt ja isend.
@ulend
---

## Teeme oma klassi

- Väga lihtne klassi (andmetüübi) kirjeldus:

```python
class Student:
    pass

s = Student()
print(type(s))  # <class '__main__.Student'>
print(id(s))    # 12448112

t = Student()
print(type(t))  # <class '__main__.Student'>
print(id(t))    # 12423408
```
@[1-2](Kirjeldame ära klassi. `pass` ei tee midagi, see on vajalik tühja sisu puhul (nt funktsioonis, if-lauses jne). Klassil on nimi `Student`)
@[1-5](Loome uue isendi e objekti)
@[1-10](Loome teise isendi. Kuigi need isendid on ühte tüüpi, on nende `id` erinev, ehk nad paiknevad mälus erinevates kohtades)

---

## Objektide võrdlemine

@ul
- Objektide võrdlemine `==` võrdlusega kontrollib vaikimisi seda, kas nad viitavad samale objektile
- Seda, mida täpselt kontrollitakse, saab üle kirjutada
  - Näiteks sõne puhul kontrollitakse seda, kas sisu (st sümbolid) on samad jne
@ulend

```python fragment
s1 = Student()
s2 = Student()
s3 = s1

print(s1 == s2)   # False
print(s1 == s3)   # True
print(s2 == s3)   # False
```

---

## Meetod

- Klassis sisalduvaid funktsioone nimetatakse meetoditeks

```python
class Student:
    """Student class."""

    def hello(self):
        """Method (function) which just prints out "Hello!"."""
        print("Hello!")


s = Student()
s.hello()       # no "self" argument
```

@[1-7](Kirjeldame klassi `Student` ja sinna sisse meetodi (funktsooni) `hello`)
@[4](Meetodil on eriline parameeter `self`, millest räägime hiljem. Seda ei pea välja kutsudes kaasa andma.)
@[1-10](Loome objekti muutujasse `s` ja kutsume objektil välja meetodi `hello()`.)
@[1-10](Nagu näha, siin argumenti kaasa ei anna. )
@[1-10](`Student` on klass, `s` on objekt (loodud `Student` klassist).)

---

## `self`

@ul
- Kõik objekti meetodid sisaldavad esimest parameetrit `self`
  - selle parameetri nimi võib ka midagi muud olla; kasutage `self`
- `self` viitab isendile
- Eelmises näites oli väljakutse `s.hello()`
  - kui `hello()` meetod käima pannakse, antakse sellele `s` kaasa
- Meetodi jaoks vajalike väärtuste jaoks lisatakse need peale `self` parameetrit
@ulend

---

## `self` ja parameetrid

```python zoom-15
class Student:
    def greet_friend(self, friend_name):
        print(f"Hello, {friend_name}")

s = Student()
s.greet_friend("Kaia")
```

@[1-2](Meetodi kirjelduses esimesel kohal on `self`, teisel kohal `friend_name`.)
@[1-6](Kui kutsume välja `greet_friend` meetodit, siis esimesena kaasa antud argument läheb teise parameetrisse jne.)

---

## Konstruktor

@ul
- Objekti loomisel pannakse käima eriline meetod ehk konstruktor
- Meetod kirjeldatakse: `\_\_init\_\_(self)`
- See meetod pannakse käima üks kord objekti loomisel
- Eelnevas näites `s = Student()` kutsub välja konstruktori
- Konstruktori kirjeldamine ei ole kohustuslik
- Konstruktor peab tagastama `None` (eraldi `return` lauset ei kirjutata).
@ulend

---

## Konstruktor

- Kirjeldatakse nagu tavaline meetod
- Eraldi pole vaja välja kutsuda

```python
class Student:
    def __init__(self):
        print("Initializing student..")

s = Student()  # Initializing student..
```

@[1-5](`Student()` kutsub `Student` klassi konstruktori välja.)

---

## Konstruktor, objekti muutujad 

@ul[ul-80]
- `self` viitab loodavale/loodud objektile
- Konstruktorisse saab kaasa anda argumente (nagu tavaline funktsioon)
- Esimene parameeter on alati `self`
- Objekti muutujad on seotud ühe konkreetse objektiga (isendiga)
- Objekti muutujaid väärtustatakse: `self.name = ...`
- Tavaliselt luuakse konstruktoris vajalikud väljad ära
- Objekti muutujaid saab teistes objekti meetodites kasutada
@ulend

---

## Konstruktor, objekti muutujad 

```python
class Student:
    def __init__(self, name, title):
        self.name = name
        self.title = title

ago = Student("Ago", "Sir")
print(ago.name)

leela = Student("Leela", "Captain")
print(leela.title)
```
@[1-4](Konstruktori parameeter `self` viitab objektile.)
@[1-4](Parameetrid `name` ja `title` salvestatakse objekti muutujateks: `self.name` ja `self.title`)
@[1-7](Loome isendi Ago. Sellel puhul määratakse objekti külge nimi ja tiitel. Saame välja printida nime.)
@[1-4,9-10](Loome isendi Leela, kelle jaoks anname teised argumendid.)

---

## Objekti muutujad

```python
class Shop:
    def __init__(self, name, age, products_file=None):
        self.products = []
        self.name = name
        self.established = 2018 - age
        if products_file is not None:
            # open the file and read products from it
            pass

    def inventory(self):
        print(f"Inventory for {self.name} (est. {self.established}:")
        for p in self.products:
            print("product: ..")
```
@[1-8](`name` muutuja salvestatakse objekti muutujaks)
@[1-8](`age` muutuja kasutatakse `self.established` väärtuse arvutamiseks. Funktsiooni lõpus kaotab `age` kehtivuse.)
@[1-8](`products_file` on valikuline parameeter. Kui see on määratud, siis loetakse failist tooted.)
@[1-8](`self.products` luuakse siin tühja järjendina. Seal hakatakse hoidma kaupade nimekirja.)
@[1,9-13](`self` kaudu loodud muutujad on siin kättesaadavad: `name`, `established` ja `products`.)

---

## Klass (_class_)

- Defineerib andmetüübi
- Šabloon, mida saab hiljem kasutada, et luua konkreetseid objekte (isendeid)

```python
class Point2D:
    """Point in (x, y) coordinate space."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print(f"({self.x:.2f}, {self.y:.2f})")
```
@[1](Kirjeldab klassi `Point2D`)
@[3-5](Konstruktor, pannakse käima objekti loomisel)
@[3,7](Klassi funktsioonid ehk meetodid)

---

## Objekt (_object_)

@ul
- Konkreetne isend, instants (_instance_)
- Luuakse klassi kirjeldusest
- Klassist võib luua lõpmata palju objekte
- Samast klassist loodud objektid on sarnase struktuuriga (neil on samad meetodid ja muutujad)
- Aga igal objektil on oma olek (muutujate väärtused)
@ulend

```python fragment
p1 = Point2D(1.234, 0.23456)
p2 = Point2D(-1, 3)

p1.print_point()   # (1.23, 0.23)
p2.print_point()   # (-1.00, 3.00)
```

---

## Klass ja objekt

```python
class Point2D:
    """Point in (x, y) coordinate space)."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print(f"({self.x:.2f}, {self.y:.2f})")


p1 = Point2D(1.234, 0.23456)
p2 = Point2D(-1, 3)

p1.print_point()   # (1.23, 0.23)
p2.print_point()   # (-1.00, 3.00)
```

@[1-8](Klassi kirjeldus)
@[3](`__init__` on eriline meetod, mis käivitatakse objekti loomisel.)
@[3](`self` on esimene parameeter ja viitab objektile.)
@[4,5,8](`self.x` ja `self.y` on objekti (isendi) muutujad.)
@[11-12](Loome kaks objekti `p1` ja `p2` erinevate väärtustega.)
@[11-15](Mõlemal objektil on oma olek. Ühe oleku muutumine ei mõjuta teist.)

---

## Objektide võrdlemine

```python
p3 = Point2D(3, 3)
p4 = Point2D(3, 3)
p5 = p4

print(p3 == p4)   # False
print(p4 == p5)   # True

p3.x = 10
p3.print_point()   # (10.00, 3.00)

p4.x = 11
p4.print_point()   # (11.00, 3.00)
p5.print_point()   # (11.00, 3.00)
```
@[1-3](Loome 2 isendit `p3` ja `p4`. `p5 = p4` tähistab seda, et `p5` viitab samale isendile kui `p4` )
@[1-5](Kuigi `p3` ja `p4` väärtused on samad, siis `==` võrdlusel kontrollitakse vaikimisi, kas kaks isendit on samad (viitavad samale objektile))
@[1-6](Kuna `p5` ja `p4` viitavad samale isendile, siis siin on tulemus tõene.)
@[1-9](Muudame `p3.x` väärtust, vaid sellel isendil muutub `x` väärtus.)
@[1-14](Muudame `p4.x` väärtust, `x` väärtus muutub nii `p4` kui `p5` jaoks. Miks?)

---

## Erilised meetodid

@ul
- Python võimaldab klassis ära kirjeldada objekti käitumist erinevates olukordades
- Näiteks `\_\_eq\_\_` meetodit kasutatakse selleks, et võrrelda objekte `==` võrdlusega
- `\_\_str\_\_` meetodit kasutatakse, et saada objektist sõne kuju
- Lisaks näiteks `\_\_add\_\_(self, other)` objektide liitmiseks jne
- `\_\_lt\_\_(self, other)` väikem-kui võrdluseks
- `\_\_len\_\_(self)` kui rakendatakse `len(self)`
@ulend

---

## Objektide võrdlus

- Punkti puhul oleks mõistlik realiseerida objektide võrdlus väärtuste järgi
- Kui kahel punktil on mõlemad koordinaadid samad, siis on ka objektid võrdsed.

```python
class Point2D:
    # ...

    def __eq__(self, other):
        if isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y
        return False
```
@[1-7](Konstruktor ja `print_point` meetodid on näitest välja jäätud)
@[4](Kirjeldame `__eq__` meetodi, mis käivitatakse objektide võrdlemisel)
@[4-7](`isinstance` kontrollib, kas `other` on üldse `Point2D` tüüpi. Kui ei ole, siis ei saa punkt ka `other` objektiga võrdne olla)
@[4-7](Kui `other` on `Point2D` tüüpi, siis võrreldakse `self` ja `other` objekti `x` ja `y` koordinaate.)

---

## Objektide võrdlus

```python
p6 = Point2D(1, 2)
p7 = Point2D(1, 2)

print(p6 == p7)   # True
print(p6 is p7)   # False

p8 = p6
print(p6 is p8)   # True

```

@[1-4](Võrdleme nüüd kahte objekti `==` võrdlusega. Tulemus on tõene, kuna käivitub `__eq__` meetod, mis võrdleb sisu.)
@[1-5](Kui on vaja võrrelda, kas kaks muutujat viitavad samale isendile, siis kasutada `is` võrdlust)
@[1-8](Kuna `p8` viitab samale objektil kui `p6`, siis võrdlus `p6 is p8` annab tulemuseks `True`)

---

## Objekt sõnena

@ul[ul-80](false)
- `\_\_str\_\_(self)` meetod võimaldab kirjeldada, mida objekti puhul sõnena tagastatakse
- Näiteks printimisel kasutatakse seda
- Samuti `str(obj)` puhul.
- Meetod tagastab sõne
- Vaikimisi `print(p1)` kuvab midagi sellist `<\_\_main\_\_.Point2D object at 0x0050D5D0>`.
@ulend

```python
class Point2D:
    # ...
    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"
        
p1 = Point2D(1, 2)
print(p1)           # (1.00, 2.00)
```

---

## Objekt sõnena

@ul
- Pythonis on eriline meetod `\_\_repr\_\_`, mille eesmärk on tagastada üheselt mõistetav sõne.
  - Tihti tagastatakse sõne, millega saab objekti luua `eval()` funktsiooni abil
- Kui `\_\_str\_\_` pole defineeritud, kutsutakse `\_\_repr\_\_` välja.
- `\_\_str\_\_` meetodi eesmärk on pigem olla informatiivne
- Seega alati on mõistlik kirjeldada `\_\_repr\_\_`
@ulend

```python fragment
class Point2D:
    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"
```

---

## Klassi muutujad

@ul
- Klassi muutuja kirjeldatakse klassi sees väljaspool meetodeid
- Klassi muutujal on üks väärtus läbi terve programmi
- Sõltumata sellest, mitu objekti klassist luuakse, klassi muutujal on üks ühine väärtus
- Üldiselt ei ole vaja kasutada
@ulend

---

@snap[north span-100]
## Klassi muutuja näide
@snapend

@snap[west span-53]
```python

class Doorbell:
    click_count = 0

    def __init__(self):
        self.click_count = 0

    def ring(self):
        print("Ringing..")
        self.click_count += 1
        Doorbell.click_count += 1
```
@snapend

@snap[east span-53]
```python
d1 = Doorbell()
d2 = Doorbell()

for _ in range(10): d1.ring()
for _ in range(4): d2.ring()
print(d1.click_count)         # 10
print(d2.click_count)         # 4
print(Doorbell.click_count)   # 14
```
@snapend

@snap[south span-100]
@[12, 13](Loome kaks uksekella `d1` ja `d2`)
@[15,16](Helistame esimest 10 ja teiset 4 korda.)
@[1-10](Klassi muutuja ja objekti muutuja võivad sama nimega olla - need ei lähe omavahel segamini.)
@[1-10](Klassi muutuja on seotud klassiga, objekti muutuja iga objektiga.)
@[1-10](`ring()` meetodis suurendame konkreetse uksekella vajutamiste arvu `self.click_count += 1`.)
@[1-11](Ühtlasi muudame klassi muutujat `Doorbell.click_count += 1`.)
@snapend

---
### Objekti väärtuste pärimine/muutmine

@ul[text-08]
- Kapseldamise eesmärk on peita objekti olek maailma eest ning lubada selle muutmine vaid läbi teatud meetodite.
- Objekti väärtuste muutmiseks kasutatakse tavaliselt *getter* ja *setter* meetodeid
- See annab võimaluse kontrollida, mida ja kuidas tagastatakse/muudetakse
@ulend

```python fragment
class Student:
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
```

---

@snap[north span-100]
## `@property` dekoraator

@ul[text-07]
- Python pakub mugavama viisi, kuidas *getter* ja *setter* meetodeid kirjeldada
- Kasutame dekoraatorit `@property`
  - lisatakse meetodi kirjelduse ette
@ulend
@snapend

@snap[south-west span-60]
```python fragment zoom-07

class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def name(self):
        # some optional calculation for name
        return f"{self.firstname} {self.lastname}"

    @name.setter
    def name(self, name):
        # some optional validation
        self.firstname, self.lastname = name.split(" ")
```
@snapend

@snap[south-east span-40]
```python fragment zoom-08

if __name__ == '__main__':
    s = Student("Ago", "Luberg")
    s.name = "Ain Kaasik"
    print(s.name)  # Ain Kaasik
```
@snapend

---

## Pärimine

@ul[text-09]
- Klass võib pärida osa (või kõiki) atribuute (omadusi ja meetodeid) teistelt klassidelt
- Näiteks klass "loom" omab üldisi atribuute looma kohta (näiteks käppade, jalgade, käte arv; meetodid "söö", "tee häält")
- Klass "koer" võib pärida kõik klassi "loom" atribuudid
- Lisaks võib "koer" klassis:
  - täiendavaid atribuute lisada (näiteks "kas haugub")
  - mõne meetodi üle kirjutada ("tee häält" teeb haukumise häält)
- Pärimise kohta öeldakse ka laiendamine
@ulend

---

## Pärimine

```python
class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
        
p3d = Point3D(1, 2, 3)
print(p3d)     # (1.00, 2.00)
```

@[1](Klass `Point3D` laiendab klassi `Point2D`.)
@[1-4](`super()` pöördub ülemklassi (st `Point2D`) poole. Siin kutsutakse välja `Point2D` konstruktor)
@[1-7](Miks tulemus on (1.00, 2.00)?)

---

## Pärimine

@ul[text-08]
- Kui pöördume objekti meetodi/muutuja poole, siis:
  - kõigepealt otsitakse meetodit/muutujat objekti klassist
  - kui objekti klassis seda ei leidu, otsitakse ülemklassist
  - kui ülemklassist ei leidu, siis ülemklassi ülemklassist jne
- Seega, kui alamklassis sama nimega meetod kirjutda, "peidab" see ülemklassi meetodi ära
@ulend

```python fragment
class Point2D:
    # ...
    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"
```
@[1-4](Kuna `Point3D` klassis pole `__str__` meetodit, pöördutakse ülemklassi ehk `Point2D` poole.)

---

## Pärimine

```python
class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

p3d = Point3D(1, 2, 3)
print(p3d)     # (1.00, 2.00, 3.00)
```

@[6-7](Lisame siia `__str__` meetodi.)
@[1-10](Nüüd kuvatakse õige tulemus)

---

## Nimetamine

@ul[text-08]
- Klassi nimes kasutatakse reeglina _Upper Camel Case_ formaadis (sõnad kokku kirjutatud, iga sõna algab suure tähega):
 - `AlmightyRobot`, `MapObject`
 - Erindid on klassid, seega tuleb neid samamoodi nimetada: `NoMoreMoves`, `PrincessException`
- Meetodi nimi väikeste tähtedega, sõnade vahel alakriips: `get_area()`
- Meetodid ja muutujad, mis algavad alakriipsuga, pole mõeldud avalikuks kasutamiseks (n-ö privaatsed).
 - `_internal_counter`, `_calculate_raw_price()`
- Kaks alakriipsu on veel rangem "soovitus"
  - kuigi Python lubab neid kasutada ka väljaspool objekti
@ulend

---

Viited:

- https://ained.ttu.ee/pydoc/classes.html
- https://docs.python.org/3/tutorial/classes.html
