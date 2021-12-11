from PIL import Image, ImageDraw, ImageFont
import math, random

x1 = 612
y1 = 612

def auto_color():
    d = 0
    rgbGenerator = lambda: (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        100,
    )
    color = rgbGenerator()
    luminance = (0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]) / 255
    if luminance > 0.5:
        d = 0
    else:
        d = 255
    return [(d, d, d), color]


def convert(quote, author, fg=None, bg=None):
    if bg:
        bg = bg
    else:
        bg = (0, 0, 0)
    if fg:
        fg = fg
    else:
        fg = (255, 255, 255)
    sentence = f"{quote} - {author}"

    quote = ImageFont.truetype("fonts/Coves Bold.otf", 27)

    img = Image.new("RGB", (x1, y1), color=bg)
    d = ImageDraw.Draw(img)

    sum = 0
    for letter in sentence:
        sum += d.textsize(letter, font=quote)[0]
    average_length_of_letter = sum / len(sentence)

    number_of_letters_for_each_line = (x1 / 1.618) / average_length_of_letter
    incrementer = 0
    fresh_sentence = ""

    for letter in sentence:
        if letter == "-":
            fresh_sentence += "\n\n" + letter
        elif incrementer < number_of_letters_for_each_line:
            fresh_sentence += letter
        else:
            if letter == " ":
                fresh_sentence += "\n"
                incrementer = 0
            else:
                fresh_sentence += letter
        incrementer += 1
    dim = d.textsize(fresh_sentence, font=quote)
    x2 = dim[0]
    y2 = dim[1]

    qx = x1 / 2 - x2 / 2
    qy = y1 / 2 - y2 / 2

    d.text((qx, qy), fresh_sentence, align="center", font=quote, fill=fg)

    return img
