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
- `git add <file>` - seab faili valmis
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

@ul[ul-90]
- Failid projekti kaustas ei ole automaatselt Giti jälgimise all
- `git add <file>` valmistab faili ette
- Sedasi võib mitu faili lisada
- `git commit -m "comment"` salvestab kohalikku salve lisatud failide muudatused (hetketõmmis)
- Kehtestuse ajal lisatakse kommentaar
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

@ul[ul-80]
- Kui arendad mitmes arvutis või projektiga töötab mitu inimest, võib tekkida seis, kus kohalikus arvutis pole kõiki viimaseid uuendusi.
- Näiteks tegid kooliarvutis ühe ülesande ära ja lisasid serverisse; koduarvutis on aga vana seis (mis oli enne tundi).
- Seega tuleb koduarvutis tõmmata uus seis alla serveris
- `git pull` - tõmbab serverist viimase seisu
@ulend

---

## Server vs kohalik

@ul
- Serveris ja kohalikus arvutis on failist sama versioon 10.
- Kui keegi lisab serverisse failist uue versiooni 11
- Kohalikus arvutis on versioon 10, peale uuendamist tekib versioon 11
- Kohalik versioon 11 ja serveri versioon 11 aga ei ühildu - tekib konflikt
- Konflikte on võimalik lahendada
@ulend

---

## Konflikt

![Git conflict](git/git-conflict.png)

---

## Pull and push

![Git conflict](git/git-pull-and-push.png)

---

## Võimalikud konfliktid

@ul
- Kindlam: alati enne arendamist tee `git pull`
- Kui tekib konflikt, võib vaja olla käsitsi lahendamist (nii sinu kui serveri muudatused pannakse kokku ühte faili)
- Teine võimalus: teha `git clone` mõnda teise kausta ja kopeerida uued failid/muudatused uuesti
- Konfliktide lahendamist siin aines väga ei käsitleta
@ulend

---

![Git fire](git/git-fire.png)
