from PIL import Image
import random


def main():
    size = (1000, 1000)
    img = Image.new("RGB", size, 0)
    triangle = [(size[0]//2, 50), (50, size[1]-50), (size[0]-50, size[1]-50)]
    point = (300, 600)
    for _ in range(1000000):
        random_vertex = random.randint(0, 2)
        point = (point[0] + ((triangle[random_vertex][0] - point[0]) // 2),
                 point[1] + ((triangle[random_vertex][1] - point[1]) // 2))
        img.putpixel(point, (255, 0, 0))
    img.save("sierpinski.png")


if __name__ == "__main__":
    main()