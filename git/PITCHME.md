## Git

---

## Git

@ul
- Versioonihaldussüsteem (_version control system, VCS_)
- Kasutatakse muudatuste jälgimiseks failides
- Kasutatakse koodi jagamiseks mitme arendaja vahel
- Saab vaadata, kes ja millal on muudatusi teinud
- Saab taastada sobiva seisu ajaloost
- Kohalik ja kaugsalv
@ulend

---

## Kuidas töötab

@ul
- Hoiab meeles koodi ajalugu
- Teeb hetketõmmise (_snapshot_) failidest
- Arendaja otsustab, millal tõmmist teha, kasutades kehtestust (_commit_)
- Saab vaadata kõiki hetketõmmiseid
- Failid pannakse eelnevalt valmis (_stage_)
@ulend

---

## Põhikäsud

@ul
- `git init` -  loob kohaliku salve (_repository_)
- `git add <file>` - seab valmis faili
- `git status` - näitab, mis failid on valmis seatud (muutused)
- `git commit` - kehtestab ettevalmistatud muudatused (failid)
- `git push` - saadab kehtestused välisesse serverisse
- `git pull` - tõmbab viimase seisu serverist
- `git clone` - kloonib salve serverist
@ulend

---

## Paigaldamine

https://git-scm.com/

- Linuxis on kas peal või kasuta mõnda pakkide paigaldamise tööriista (apt-get, yum, etc)

---

## Kasutamine (aines)

@ul
- Alustame salve (projekti) loomisega gitlab.cs.ttu.ee lehel
- Kloonime tühja salve arvutisse: `git clone <url>`
- Luuakse kaust vastavalt projekti nimele
- Kaustas on `.git` kaust, kus hoitakse vajalikke faile Giti jaoks
@ulend

---

## Faili lisamine serverisse

@ul
- Kui fail on projekti kaustas, ei ole see automaatselt Giti jälgimise all
- `git add <file>` lisab faili jälgimisse / valmistab faili ette
- Sedasi võib mitu faili lisada
- `git commit` salvestab kohalikku salve lisatud failide muudatused (hetketõmmis)
- Kehtestuse ajal on vaja lisada ka kommentaar `git commit -m "comment"`
- `git push` lisab kõik kohalikud muudatused serverisse
@ulend

---

## Muudatuse saatmine serverisse

@ul
- Muudetud failid automaatselt Giti ei jõua
- `git add <file>` lisab faili _staging_ staatusesse
- `git commit` lisab faili kohalikku salve
- `git push` saadab muudatused serverisse
@ulend

---

## Git PyCharmis

@ul
- Kui fail on korra Giti lisatud (`git add`), siis seda sammu järgmiste kehtestuste ajal tegema ei pea
- `commit` ja `push` võimalik teha peaaegu ühe klikiga
@ulend

---

## Serverist seisu tõmbamine

@ul
- Kui arendad mitmes arvutis või projektiga töötab mitu inimest, võib tekkida seis, kus kohalikus arvutis pole kõiki viimaseid uuendusi.
- Näiteks tegid kooliarvutis ühe ülesande ära ja lisasid serverisse; koduarvutis on aga vana seis (mis oli enne tundi).
- Seega tuleb koduarvutis tõmmata uus seis alla serveris
- `git pull` - tõmbab serverist viimase seisu
@ulend

---

