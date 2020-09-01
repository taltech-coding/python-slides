## ITI0102 - Programmeerimise algkursus
#### Loeng 1 - Korraldus
##### Ago Luberg

---

## Kokkuvõte

@ul 

- 8 loengut (paaritu nädal T12)
- 16 praktikumi: T14, N8, N9:45, N16:10 
- 8 süvendatud praktikumi: paaris T12 
- Kursuse jooksul lahendate ülesandeid **iseseisvalt**
- Ülesande lahendamine ja **ettenäitamine** annab punkte 
- Punktid liidetakse 
- Semestri jooksul 400 punkti 
- Eksam 600 punkti 
- Kokku 501p - 600p => "1", ... 901p - .. => "5" 

@ulend

---

## Konsultatsioon

- Kasutage täiendusõppe tunde (E14, E16, R8:15, R10)

---

## Ainele registreerimine

- moodle.taltech.ee -> uniid login
- suunatakse Microsofti lehele
 - email: uniid@ttu.ee (nt aglube@ttu.ee)
  - sellega saate ühtlasi oma e-kirju lugeda mail.ttu.ee lehel
 - parool (kui ei tea, siis pass.ttu.ee lehel saate luua/muuta)
- otsige aine "ITI0102 - Programmeerimise algkursus"
- registreeruge (*enrol*)

---

## Ainele registreerimine

- Kasutage võtit: 
 - `IAAB`
 - `IADB`
 - `IADB-SESS`
 - `IAIB`
 - `MUU` (muu õppekava)
 - `VABA` (ilma deklaratsioonita)

---


## Ülesanded

@ul

- Iga nädal kaks ülesannet
  - PR - lihtsam ülesanne
  - EX - mahukam ülesanne
- Automaattestimine
- Kokku 15 nädalat

@ulend

---

## Ülesannete tähtajad

@ul

- Ülesande tähtaeg järgmise nädala teisipäev kell 09:00
- EX ülesande puhul iga 24h-ga -10%
- PR ülesande puhul peale tähtaega nädal aega -50%, edasi 0

- Näiteks EX01 tähtaeg on 8. september 09:00 (saab kuni 100%)
- kuni 13. september 09:00 saab kuni 50%
- alates 17. septembrist 0p

@ulend

---

## Ülesande esitamine

@ul

- Ülesande lahendus laetakse Giti
- Tudeng saab esitatud ülesande kohta TTÜ emailile tagasisidet (näiteks 80% punktidest)
- Lahendust võib üles laadida (esitada) lõpmatu arv kordi (kui pole öeldud teisiti)
- Arvesse läheb parim (kui pole öeldud teisiti)
- Punktid lähevad arvesse alles pärast seda, kui lahendus on õppejõule ette näidatud

@ulend

---

## Ülesande ettenäitamine

@ul[ul-80]

- Ettenäitamisel veendume, et tudeng saab **enda** kirjutatud koodist aru
- Ettenäitamisel anname tudengi koodile tagasisidet
- Ettenäitamise eest on (väga harva) võimalik saada trahvipunkte
  - kui tudeng ei saa **enda** koodist aru
  - kood on väga ebapraktiline
- Tavaliselt antakse tudengile võimalus koodi parandada

@ulend

---

## Ülesande punktid

@ul

- Lõpptulemus sõltub kolmest komponendist:
 - automaattestid (100% =>15p; 80% => 13p)
 - stiilikontroll (korras => 1p, üks viga => 0)
 - ettenäitamine kuni 1p
- Saadud komponendid korrutatakse
 - näiteks: `13 x 1 x 1 => 13p`.
- Kui stiil on korrast ära, siis on kokku 0p
- Kui ülesanne pole ette näidatud, siis on kokku 0p

@ulend

---

## Automaatne stiilikontroll

@ul[ul-80]

 - Kõik lahendused peavad vastama stiilinõuetele
 - Kasutame aines kahte kontrolli:
   - [PEP 8](https://www.python.org/dev/peps/pep-0008/) - Üldine koodistiil
   - [PEP 257](https://www.python.org/dev/peps/pep-0257/) - Dokumenteerimise stiil
 - Funktsioonid, klassid, meetodid jms peavad olema kommenteeritud
   - Sisu kontrollime ka ("asd" võib automaattesterile sobida, aga õppejõule mitte!)
 - Automaattester annab stiilivigadest teada

@ulend

---

## Süvapython

@ul

- Mõne jaoks on tavaülesanded igavad
- Pakume võimalust lahendada keerukamaid ülesandeid
- Kokku semestri jooksul umbes 8 ülesannet
- Nende eest saab kokku 100p
- "5" saamiseks tuleb neid lahendada
- Teemadest räägime paaris teisipäeval kell 12.00

@ulend

---

## Punktid kokku

@ul

- Ülesanded 400p
 - PR ülesanded 15 x 5p = 75p
 - EX ülesanded 15 x 15p = 225p
 - süvaülesanded 100p
- Eksam 600p
- Kokku: 1000p
- Kui süva ülesandeid ei tee, siis kokku 900p
- 901p -> "5", 801p -> "4", ... 501p -> "1", <501p -> "0" 

@ulend

---

## Tunnikontroll, Kontrolltöö

@ul

* 5\. nädalal tunnikontroll (TK)
  * antakse 5 ülesannet
  * vähemalt pooled punktid tuleb saada (50%)
  * 5p (PR ülesande asemel)
* 10\. nädalal kontrolltöö (KT)
  * vähemalt pool tuleb ära teha (50%)
  * 20p (PR ja EX ülesande asemel)

@ulend

---

## Eksam

@ul

- **Eksamieeldus:**
  - vähemalt 200p
  - TK 50%, KT 50%
- Eksam toimub arvutiga
- Lahendatakse ülesandeid + *quiz*
- Interneti kasutamine pole lubatud
- Aega 4h

@ulend

---

## Nädalate teemad

* 1n Sissejuhatus, muutuja, tingimuslause, sisendi lugemine
* 2n funktsioon, matemaatilised avaldised
* 3n sõne, tsükkel
* 4n järjend, tsükkel, sõnastik
* 5n Tunnikontroll, sõnastik
* 6n objekti mõiste
* 7n OOP
* 8n failid (lugemine, kirjutamine), sortimine, testimine

---

## Teemad (jätkub)


* 9n Rekursioon
* 10n Kontrolltöö
* 11n Objektid, klassid
* 12n Objektid, klassid, pärimine
* 13n Veebist lugemine, API
* 14n OOP + välised teegid
* 15n Vaba struktuuriga OOP
* 16n Kordamine

---

## Täiendusõpe

@ul
- Esimesed 5 nädalat toimub abistav kursus ITI0002 - Programmeerimise täiendusõpe
- Iga nädal 2 praktikumi (kokku 5 x 2 = 10 praktikumi)
- Aine on arvestuslik (2 EAP)
- Arvestuse saamiseks tuleb käia kohal
- Aine on tasuta
- See ei ole kohustuslik aine

@ulend

---

## Täiendusõpe - arvestus

@ul
- Arvestuse saamiseks:
  - tuleb lahendada ära antud ülesanded 7. nädalaks
  - tuleb sooritada algkursuse tunnikontroll (5. nädalal)

@ulend

---

## Täiendusõpe - korraldus

@ul
- Anname hulk ülesandeid, mida saate lahendada
- Abiõppejõud aitavad küsimuste korral
- Lahendame mõned ülesanded ka ekraanil läbi
- Üldiselt on ülesanded teemade kaupa (1. tund näiteks muutuja, printimine, sisendi lugemine)
- Ülesannetel pole konkreetseid tähtaegu
- Soovitatav oleks t01 lahendada enne t02-e ära jne
@ulend

---

## Täiendusõpe

@ul
- Kui sa oskad programmeerida (näiteks suudad CodingBat ülesanded ära lahendada), siis seda ainet pole sulle vaja.
- See on justkui konsultatsioon, mis on tunniplaanis kirjas
- Peale 5. nädalat jätame arvatavasti ühe aja konsultatsiooniks
- Kasutame neid tunde, et teemadest rääkida
@ulend

---

## Küsimused?

---

## Materjalid

@ul
- moodle.taltech.ee - kursuse info, ülesanded jms (ka kõik viited võiks siia jõuda)
- discord chat: https://discord.gg/EckUYf6
- õppematerjal: https://ained.ttu.ee/pydoc/
- YouTube videod: https://www.youtube.com/c/TalTechCoding
- Ülesandeid harjutamiseks: https://codera.cs.ttu.ee ja http://codingbat.com
@ulend

---
## Onboarding

- https://cs.ttu.ee/onboarding/python/
- 326 tudengid on täitnud
- 244 nendest jõudsid lõpuni
- Kui Sa pole veel täitnud, palun tee seda!
- Keskmine hinne protsessile 9.2

---

## Täna tunnis

@ul
- See presentatioon
- Teeme algust Pythoni teemadega..
  - Python
  - print-input
  - muutuja
  - tingimuslause
@ulend

---

## Küsimused?
