import time

current_time = int(time.time())

generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

print("generated number:{}".format(generated_number))

import matplotlib.pyplot as pyplot
from PIL import Image
from os import path

ASSIGNMENT_FOLDER = "Assignment 2"
IMG_SRC = path.join(path.dirname(__file__), ASSIGNMENT_FOLDER, "chapter1.png")
IMG_OUTPUT = path.join(path.dirname(__file__), "chapter1out.png")

image = Image.open(IMG_SRC)
width = image.size[0]
height = image.size[1]

pyplot.imshow(image)
img_px = image.load()

coordinates = []
pixels = []
sum = 0
for x in range(width):
    for y in range(height):
        rgb = img_px[x, y]
        coordinates.append([x, y])
        pixels.append(
            (
                rgb[0] + generated_number,
                rgb[1] + generated_number,
                rgb[2] + generated_number,
            )
        )
        sum += rgb[0] + generated_number

import pandas

column = ["Coordinates", "RGB"]
df = pandas.DataFrame(zip(coordinates, pixels), columns=column)

from PIL import ImageDraw

img_out = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(img_out)

for row in df.itertuples(index=True):
    draw.point(row.Coordinates, row.RGB)
img_out.save(IMG_OUTPUT)

print(sum)
