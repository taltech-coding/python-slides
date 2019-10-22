## ITI0102 - Programmeerimise algkursus
### Pilditöötlus
#### _image processing_

---

## Pillow installeerimine PyCharmis

- PyCharm
 - File -> Settings -> Project -> Project Interpreter
 - "+" (install)
 
![List of packages](image/packages.png)

---

## Pillow installeerimine PyCharmis

- Otsi "Pillow"
- Vali "Pillow" pakett
- "Install package"
 
![Install package](image/install_package.png)

---

## Installeerimine pip-iga

- pip skript võimaldab installida pakke, mis on PyPIs (https://pypi.python.org/pypi) (~200k pakki)
- pip installimine
 - uuemate pythonitega on pip kaasas (versioon >=3.4)
 - muul juhul https://pip.pypa.io/en/stable/installing/
- Python 3 puhul on tavaliselt skripti nimi pip3
- Paki installimine:
  `pip install package`
- Pillow jaoks:
  `pip install pillow`
  
---

## Pillow

- Aktiivne haru (_fork_) PIL pakile
 - PIL viimane versioon aastast 2009
 - Python 3 tugi puudus
- Pillow viimane versioon 6.2.1 (21. oktoober 2019)
- Dokumentatsioon: https://pillow.readthedocs.io

---

## Koodinäide

```python

from PIL import Image
from PIL import ImageDraw

width = 100
height = 100
steps = 10
step = width / steps
img = Image.new('RGB', (100, 100))
draw = ImageDraw.Draw(img)
for i in range(steps):
    draw.rectangle((i * step, i * step, (i + 1) * step - 1, (i + 1) * step - 1), fill=(128, 110, 200))
del draw   # let's remove draw object from memory
img.save("test.png", "PNG")

```

![List of packages](image/test.png)

---

## Alternatiivsed vahendid

- Testserveris praegu muid pakke pole
- Kui kellelgi on mõni ettepanek, mida võiks kasutada, siis kaalume
- Tööriistu, mille eesmärk on muu (nt pygame, opencv jms), ei hakka testserverisse installima

---

## Pildinäide (Eesti)

![List of packages](image/eesti_2017.png)

---

## Pildinäide (maailm)

![List of packages](image/world.png)