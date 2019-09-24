## ITI0102 - Programmeerimise algkursus
### Regulaaravaldis
#### _Regular expression_

---

## Regulaaravaldis

- Regulaaravaldis (_regular expression_) kirjeldab ära mustri (_pattern_)
- Mustrit saab kasutada otsinguks ja teksti asendamiseks
- Võimaldab rohkem kui "otsi alamsõne X tekstist Y"

---

## `re` moodul

```python
import re

match = re.search("abc", "aabca")
print(match.group())  # abc is found in text
match = re.search("xyz", "aabca")
print(match is None)  # no match

```

@[3](Otsitakse mustrit "abc" tekstist "aabca")
@[3-4](`re.search` tagastab `Match` objekti, kus on täiendav info sees.)
@[5-6](Kui mustrit ei leita tekstist, tagastatakse `None`.)
---

## Muster

@ul[many-items]

- Muster koosneb metamärkidest (erilise tähendusega sümbolid) ja tavalistest sümbolitest (otsese tähendusega)
- Muster võib koosnevad teistest (alam)mustritest
 - Kui `A` ja `B` on mustrid, siis ka `AB`, `BA`, `AAB`, `ABB` jne on mustrid
- Alammustreid tavaliselt eraldatakse sulgudega: `A((B)C)`
- Mustrile vastavat alamsõne tekstist nimetatakse vasteks
- Mustrit saab kasutada:

  - et kontrollida, kas mingi sõne vastab reeglitele / mustrile (kas email on korrektne)
  - leida üles mingile mustrile vastav sõne (näiteks kõik emailid)

@ulend

---

## Muster kui alamsõne

- Muster võib olla alamsõne, millele otsitakse täpset vastet tekstist
- Üldiselt sellisel juhul mõistlikum kasutada `sub in text` (kiirem)

Näide: `"`@css[u](`abc`)`"`

Sisalduv tekst: @css[match](`"a`)@css[match-u](`abc`)@css[match](`a"`)

Mittesisalduv tekst: @css[nomatch](`"ababac"`)

---

## Suvaline sümbol

- Vastab ühele suvalisele sümbolile

Muster: `.`

Näide: `"`@css[u](`a.bc`)`"`

Sisalduv tekst: @css[match](`"`)@css[match-u](`a2bc`)@css[match](`a"`)

Mittesisalduv tekst: @css[nomatch](`"abc"`)

---

## Algus

- Tähistab sõne algust

Muster: `^`

Näide: `"`@css[u](`^abc`)`"`

Sisalduv tekst: @css[match](`"`)@css[match-u](`abc`)@css[match](`d"`)

Mittesisalduv tekst: @css[nomatch](`"aabc"`)

---

## Lõpp

- Tähistab sõne lõppu

Muster: `$`

Näide: `"`@css[u](`abc$`)`"`

Sisalduv tekst: @css[match](`"aa`)@css[match-u](`abc`)@css[match](`"`)

Mittesisalduv tekst: @css[nomatch](`"abca"`)

---

## 0 või 1 kord

- Eelnevat alammustrit on 0 või 1 kord

Muster: `?`

Näide: `"`@css[u](`ab?c`)`"`

Sisalduv tekst: @css[match](`"a`)@css[match-u](`ac`)@css[match](`a"`)

Sisalduv tekst: @css[match](`"a`)@css[match-u](`abc`)@css[match](`a"`)

Mittesisalduv tekst: @css[nomatch](`"aabbcc"`)


---

## 0 või rohkem kordi

- Eelnevat alammustrit on 0 või rohkem korda

Muster: `*`

Näide: `"`@css[u](`ab*c`)`"`

Sisalduv tekst: @css[match](`"a`)@css[match-u](`ac`)@css[match](`a"`)

Sisalduv tekst: @css[match](`"a`)@css[match-u](`abc`)@css[match](`a"`)

Sisalduv tekst: @css[match](`"a`)@css[match-u](`abbbc`)@css[match](`a"`)

Mittesisalduv tekst: @css[nomatch](`"abab"`)

Mittesisalduv tekst: @css[nomatch](`"bbc"`)

---

## 1 või rohkem kordi

- Eelnevat alammustrit on 1 või rohkem korda

Muster: `+`

Näide: `"`@css[u](`ab+c`)`"`

Sisalduv tekst: @css[match](`"a`)@css[match-u](`abc`)@css[match](`a"`)

Sisalduv tekst: @css[match](`"a`)@css[match-u](`abbbc`)@css[match](`a"`)

Mittesisalduv tekst: @css[nomatch](`"aac"`)

Mittesisalduv tekst: @css[nomatch](`"abbba"`)

---

## Varjestamine (_escape_)

- Järgnevat erilist sümbolit tõlgendatakse ilma tähenduseta

Muster: `\`

Näide: `"a`@css[u](`\.`)`bc"`

Sisalduv tekst: @css[match](`"a`)@css[match-u](`.`)@css[match](`bc"`)

Mittesisalduv tekst: @css[nomatch](`"a`)@css[nomatch-u](`2`)@css[nomatch](`bc"`)

---

## Kordub _m_ korda

- Alammustrit kordub täpselt `m` korda

Muster: @css[pat](`{m}`)

Näide: `"a`@css[u](`a{2}`)`c"`

Sisalduv tekst: @css[match](`"aa`)@css[match-u](`bb`)@css[match](`cc"`)

Mittesisalduv tekst: @css[nomatch](`"aacc"`)

Mittesisalduv tekst: @css[nomatch](`"aa`)@css[nomatch-u](`b`)@css[nomatch](`cc"`)

Mittesisalduv tekst: @css[nomatch](`"aa`)@css[nomatch-u](`bbb`)@css[nomatch](`cc"`)

---

## Kordub _m_-_n_ korda

- Alammustrit kordub `m` - `n` korda

Muster: @css[pat](`{m,n}`)

Näide: `"a`@css[u](`b{2,3}`)`c"`

Sisalduv tekst: @css[match](`"aa`)@css[match-u](`bb`)@css[match](`cc"`)

Sisalduv tekst: @css[match](`"aa`)@css[match-u](`bbb`)@css[match](`cc"`)

Mittesisalduv tekst: @css[nomatch](`"aacc"`)

Mittesisalduv tekst: @css[nomatch](`"aa`)@css[nomatch-u](`b`)@css[nomatch](`cc"`)

Mittesisalduv tekst: @css[nomatch](`"aa`)@css[nomatch-u](`bbbb`)@css[nomatch](`cc"`)


---

## Sobiv hulk

- Sobivad sümbolid antud hulgast

Muster: @css[pat](`[..]`)

Näide: `"`@css[u](`[ab]`)`cd"`

Sisalduv tekst: @css[match](`"`)@css[match-u](`a`)@css[match](`cd"`)

Sisalduv tekst: @css[match](`"`)@css[match-u](`b`)@css[match](`cd"`)

Mittesisalduv tekst: @css[nomatch](`"cd"`)

Mittesisalduv tekst: @css[nomatch](`"`)@css[nomatch-u](`c`)@css[nomatch](`cd"`)

---

## Sobiv vahemik

- Sobivad sümbolid antud vahemikust

Muster: @css[pat](`[.-.]`)

Näide: `"`@css[u](`[a-c]`)`de"`

Sisalduv tekst: @css[match](`"`)@css[match-u](`a`)@css[match](`de"`)

Sisalduv tekst: @css[match](`"`)@css[match-u](`b`)@css[match](`de"`)

Sisalduv tekst: @css[match](`"`)@css[match-u](`c`)@css[match](`de"`)

Mittesisalduv tekst: @css[nomatch](`"de"`)

Mittesisalduv tekst: @css[nomatch](`"`)@css[nomatch-u](`d`)@css[nomatch](`de"`)

---

## Miinus hulgas

- Miinusmärgi võib varjestada

Näide: `"`@css[u](`[a\-c]`)`cd"`

Sisalduv tekst: @css[match](`"`)@css[match-u](`a`)@css[match](`cd"`)

Sisalduv tekst: @css[match](`"`)@css[match-u](`c`)@css[match](`cd"`)

Sisalduv tekst: @css[match](`"`)@css[match-u](`-`)@css[match](`cd"`)

Mittesisalduv tekst: @css[nomatch](`"cd"`)

Mittesisalduv tekst: @css[nomatch](`"`)@css[nomatch-u](`b`)@css[nomatch](`cd"`)

---

## Miinus hulgas 2

- Miinusmärgi võib panna esimeseks/viimaseks

Näide: `"`@css[u](`[ac-]`)`cd"`

Sisalduv tekst: @css[match](`"`)@css[match-u](`a`)@css[match](`cd"`)

Sisalduv tekst: @css[match](`"`)@css[match-u](`c`)@css[match](`cd"`)

Sisalduv tekst: @css[match](`"`)@css[match-u](`-`)@css[match](`cd"`)

Mittesisalduv tekst: @css[nomatch](`"cd"`)

Mittesisalduv tekst: @css[nomatch](`"`)@css[nomatch-u](`b`)@css[nomatch](`cd"`)

---

## Grupeerimine

- Võimaldab grupeerida pikema alammustri

@css[pat](parenthesis test (&#41;)

Muster: @css[pat](`(...&#41;`)

Näide: `"`@css[u](`(ab`&#41;`?cd`)`"`

Sisalduv tekst: @css[match](`"a`)@css[match-u](`cd`)@css[match](`e"`)

Sisalduv tekst: @css[match](`"`)@css[match-u](`abcd`)@css[match](`e"`)

Sisalduv tekst: @css[match](`"abb`)@css[match-u](`cd`)@css[match](`"`)

Mittesisalduv tekst: @css[nomatch](`"ab`)

Mittesisalduv tekst: @css[nomatch](`"`)@css[nomatch-u](`d`)@css[nomatch](`de"`)

---

## Või

- Valik mustritest

Muster: @css[pat](`|`)

Näide: `"(ab|cd)+ef"`

Sisalduv tekst: @css[match](`"`)@css[match-u](`abef`)@css[match](`g"`)

Sisalduv tekst: @css[match](`"`)@css[match-u](`cdef`)@css[match](`g"`)

Sisalduv tekst: @css[match](`"a`)@css[match-u](`cdabef`)@css[match](`g"`)

Mittesisalduv tekst: @css[nomatch](`"acef"`)

Mittesisalduv tekst: @css[nomatch](`"abbef"`)

---

## _lookahead_, _lookbehind_

- `(?=...)`, `(?!...)`, `(?<=...)`, `(?<!...)`
- Kontrollivad, kas järgneb/eelneb märgitud muster
- Ei "kasuta" vastet ära
 - avaldis `"a(?=b)"` kasutab sõnest `"ab"` ära vaid esimese sümboli 
 - võrdluseks avaldis `"ab"` kasutab mõlemad ära
- Võimaldavad keerukamaid kontrolle

---

## Järgneb

- Alammuster peab järgnema

Muster: `(?=...)`

Näide: `"a(?=b)"`

Sisalduv tekst: @css[match](`"a`)@css[match-u](`a`)@css[match](`b"`)

Mittesisalduv tekst: @css[nomatch](`"ac"`)

Mittesisalduv tekst: @css[nomatch](`"aa"`)

---

## Ei järgne

- Alammuster ei tohi järgneda

Muster: `(?!...)`

Näide: `"a(?!b)"`

Sisalduv tekst: @css[match](`"`)@css[match-u](`a`)@css[match](`c"`)

Sisalduv tekst: @css[match](`"`)@css[match-u](`a`)@css[match](`"`)

Mittesisalduv tekst: @css[nomatch](`"acb"`)

Mittesisalduv tekst: @css[nomatch](`"b"`)

---

## Eelneb

- Alammuster peab eelnema

Muster: `(?<=...)`

Näide: `"(?<=a)b"`

Sisalduv tekst: @css[match](`"aa`)@css[match-u](`b`)@css[match](`c"`)

Mittesisalduv tekst: @css[nomatch](`"b"`)

Mittesisalduv tekst: @css[nomatch](`"acb"`)

---

## Ei eelne

- Alammuster ei tohi eelnema

Muster: `(?<!...)`

Näide: `"(?<!a)b"`

Sisalduv tekst: @css[match](`"`)@css[match-u](`b`)@css[match](`c"`)

Sisalduv tekst: @css[match](`"ac`)@css[match-u](`b`)@css[match](`"`)

Mittesisalduv tekst: @css[nomatch](`"ab"`)

Mittesisalduv tekst: @css[nomatch](`"aab"`)

---

## Grupi kattumine

- Saab kasutada eelnenud grupi kattumiseks

Muster: @css[pat](`\1, \2`)

Näide: `"(.+) \1"`

Sisalduv tekst: @css[match](`"`)@css[match-u](`a a`)@css[match](`c"`)

Sisalduv tekst: @css[match](`"1`)@css[match-u](`1 1`)@css[match](`2"`)

Sisalduv tekst: @css[match](`"`)@css[match-u](`cc cc`)@css[match](`c"`)

Mittesisalduv tekst: @css[nomatch](`"aa"`)

Mittesisalduv tekst: @css[nomatch](`"ab ba"`)

---

## Tähed, numbrid, alakriips

- Eriline sümbolite kogum

Muster: @css[pat](`\w`)

Näide: `"`@css[u](`\w+a`)`"` (`"`@css[u](`[a-zA-Z0-9_]+a`)`"`)

Sisalduv tekst: @css[match](`"`)@css[match-u](`1a`)@css[match](`"`)

Sisalduv tekst: @css[match](`"`)@css[match-u](`aa`)@css[match](`"`)

Sisalduv tekst: @css[match](`"`)@css[match-u](`baba`)@css[match](`c"`)

Mittesisalduv tekst: @css[nomatch](`"a"`)

Mittesisalduv tekst: @css[nomatch](`"a,a"`)

Mittesisalduv tekst: @css[nomatch](`" a"`)

---

## Tühik, tabulaator, reavahetus

- Eriline sümbolite kogum

Muster: @css[pat](`\s`)

Näide: `"`@css[u](`a\s{2}b`)`"`

Sisalduv tekst: @css[match](`"`)@css[match-u](`a  b`)@css[match](`"`)

Sisalduv tekst: @css[match](`"`)@css[match-u](`a\t a`)@css[match](`c"`)

Mittesisalduv tekst: @css[nomatch](`"ab"`)

Mittesisalduv tekst: @css[nomatch](`"a b"`)

Mittesisalduv tekst: @css[nomatch](`"a   b"`)

---

## Numbrid

- Eriline sümbolite kogum

Muster: @css[pat](`\d`)

Näide: `"`@css[u](`\d{2}`)`"`

Sama: `"`@css[u](`[0-9]{2}`)`"`

Sisalduv tekst: @css[match](`"`)@css[match-u](`12`)@css[match](`"`)

Sisalduv tekst: @css[match](`"a`)@css[match-u](`34`)@css[match](`c"`)

Sisalduv tekst: @css[match](`"a`)@css[match-u](`12`)@css[match](`3"`)

Mittesisalduv tekst: @css[nomatch](`"ab"`)

Mittesisalduv tekst: @css[nomatch](`"1 2"`)

Mittesisalduv tekst: @css[nomatch](`"a2"`)

---

## Ei kuulu hulka

- Sümbolid, mis ei tohi vastes olla sellel positisoonil

Muster: @css[pat](`[^..]`)

Näide: `"`@css[u](`[^a-c1-3]x`)`"`

Sisalduv tekst: @css[match](`"`)@css[match-u](`4x`)@css[match](`"`)

Sisalduv tekst: @css[match](`"a`)@css[match-u](`yx`)@css[match](`c"`)

Mittesisalduv tekst: @css[nomatch](`"ax"`)

Mittesisalduv tekst: @css[nomatch](`"1x"`)

Mittesisalduv tekst: @css[nomatch](`"cx"`)

---

## Süntaks

- Kui muster kasutab kurakaldkriipsu (`\`), tuleb see kirjutada:
 - `"\\\\"` või
 - `r"\\"`
- `r""` - _raw string_ notatsioon
- Tavalises sõnes tuleb kurakaldkriipsu jaoks kasutada kahte sümbolit `"\\"`, seejärel saab juurde lisada regulaaravaldise sümboli (näiteks `"d"`) 

---

## _raw string_

```python
import re

text = "backslash: \\"
print(text)  # backslash: \
print("match" if re.search("\\\\", text) else "no match")
print("match" if re.search(r"\\", text) else "no match")
print("match" if re.search("\\", text) else "no match")
```

@[1-4](Prindib `backslash: \`)
@[1-5](Prindib `match`)
@[1-6](Prindib `match`)
@[1-7](Annab vea, muster tõlgendab `\\` kurakaldkriipsuna, millega saab varjestada erisümboleid. Erisümbolit aga ei järgne.)

---

## _raw string_

```python

import re

print("match" if re.search("(.)\1", "aa") else "no match")
print("match" if re.search("(.)\\1", "aa") else "no match")
print("match" if re.search(r"(.)\1", "aa") else "no match")

```
@[1-3](Prindib `no match`. Miks?)
@[1-4](Prindib `match`)
@[1-5](Prindib `match`)

---

## Grupid

```python
import re

match = re.search("xk(ab)?(cd)", "xkcde")
print(match.group())
print(match.group(0))
print(match.group(1))
print(match.group(2))
```

@[1-4](Tagastab kogu vaste (sama mis küsida grupp 0-i). Kuvab `xkcd`)
@[1-5](Grupp 0 tagastab kogu vaste. Kuvab `xkcd`)
@[1-6](Grupp 1 tagastab vaste esimese sulgudepaari kohta. Antud mustris `(ab)?`. Tagastab `None`. Miks?)
@[1-7](Tagastab vaste `(cd)` kohta, ehk `cd`)

---

## Grupid

```python
import re

match = re.search("(?:ab)?(cd)e", "acde")
print(match.group())
print(match.groups())

match = re.search("(ab)?(cd)e", "acde")
print(match.group())
print(match.groups())
```

@[1-4](Tagastab `cd`. Miks mitte midagi esimeste sulgude kohta?)
@[1-4](`(?:...)` tähistab vastet mittetagastava gruppi.)
@[1-4](Kõik grupid, mis algavad `(?`, ei tagasta vastet)
@[1-5](Tagastab enniku kõikidest vastetest. Antud juhul `('cd',)`)
@[1-8](Tagastab kogu vaste (ka väljaspool gruppe). Tulemus: `cde`.)
@[1-9](Tagastab enniku. Esimesele grupile vastet ei leidu. Tulemus: `(None, 'cd')`)

---

## `match()` vs `search()`

- `match()` otsib sõne algusest
- `search()` otsib tervest sõnest

```python
import re

m1 = re.match("c", "abcdef")
m2 = re.search("c", "abcdef")

print("Match" if m1 is not None else "No match")
print("Match" if m2 is not None else "No match")
```

@[1-6](Prindib `No match`)
@[1-7](Prindib `Match`)

---

## `findall()`

- `findall()` tagastab mittkattuvate vastete (sõnede) järjendi
- `finditer()` tagastab iteraatori `Match` objektidest

```python
import re
text = "tere minu@email.ee, sõbra email on guido@baggins.com ja guits@bag.com"

emails = re.findall(r"[\w.-]+@[\w.-]+", text)
for email in emails:
    print(email)

for email in re.finditer(r"[\w.-]+@[\w.-]+", text):
    print(email.group())
```

@[1-6](`emails` on järjend kõikidest vastetest)
@[1-9](`finditer()` tagastab iteraatori (elemente tagastatakse jooksvalt vastavalt vajadusele))

---

## Viiteid

- https://docs.python.org/3/library/re.html
- https://developers.google.com/edu/python/regular-expressions
- http://rise4fun.com/Rex
  - näiteks `(ab|cd)?cd`
- https://regex101.com/
- https://regexone.com/
- https://alf.nu/RegexGolf
