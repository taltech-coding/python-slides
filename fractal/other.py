from PIL import Image
import random

def main():
    size = (1000, 1000)
    img = Image.new("RGB", size)
    point = (0, 0)
    for _ in range(10000000):
        img.putpixel((int(point[0]*100+500), int(size[1] - 1 - point[1]*100)), (0, 255, 0))
        r = random.randint(0, 3)
        if r == 0:
            point = (0, 0.16*point[1])
        elif r == 1:
            point = (0.85*point[0] + 0.04*point[1], -0.04*point[0] + 0.85*point[1] + 1.6)
        elif r == 2:
            point = (0.2*point[0] - 0.26*point[1], 0.23*point[0] + 0.22*point[1] + 1.6)
        else:
            point = (-0.15*point[0] + 0.28*point[1], 0.26*point[0] + 0.25*point[1] + 0.44)

    img.save("barnsley.png")

if __name__ == "__main__":
    main()