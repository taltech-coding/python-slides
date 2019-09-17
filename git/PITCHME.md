## Git

---

## Git

- Versioonihaldussüsteem (_version control system, VCS_)
- Kasutatakse muudatuste jälgimiseks failides
- Kasutatakse koodi jagamiseks mitme arendaja vahel
- Saab vaadata, kes ja millal on muudatusi teinud
- Saab taastada sobiva seisu ajaloost
- Kohalik ja kaugsalv

---

## Kuidas töötab

- Hoiab meeles koodi ajalugu
- Teeb hetketõmmise (_snapshot_) failidest
- Arendaja otsustab, millal tõmmist teha, kasutades kehtestust (_commit_)
- Saab vaadata kõiki hetketõmmiseid
- Failid pannakse eelnevalt valmis (_stage_)

---

## Põhikäsud

- `git init` -  loob kohaliku salve (_repository_)
- `git add <file>` - seab valmis faili
- `git status` - näitab, mis failid on valmis seatud (muutused)
- `git commit` - kehtestab ettevalmistatud muudatused (failid)
- `git push` - saadab kehtestused välisesse serverisse
- `git pull` - tõmbab viimase seisu serverist
- `git clone` - kloonib salve serverist

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
