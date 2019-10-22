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
