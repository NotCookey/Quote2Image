<h1 align="center">Quote2Image</h1>
<p align="center"><b>A Python Library to Make Quote Images</b></p>
<p align="center"><kbd><img src="https://cdn.discordapp.com/attachments/905732238237368351/919180108181422120/quote.png" height=300px></kbd></p>

# How To Use?
- **Download The Latest Package From [Releases](https://github.com/SecretsX/Quote2Image/releases)**
- **Extract The Zip File And Place Every File In It To Your Current Code Folder**

<kbd><img src="https://media.discordapp.net/attachments/905732238237368351/919182699686662204/unknown.png"></kbd>

- **Code Instructions**
```python
from Quote2Image import auto_color, convert

# Automatically Generates a Perfect Match of Colors for Fore and Back
color=auto_color()

img=convert(quote="Pooing keeps you healthy",author="Pee",fg=color[0],bg=color[1])

# Save The Image as a Png file
img.save("quote.png")

# Everytime you run this code it will generate a quote.png file with a different background and foreground
```

# That's It!
> Thank You! Hope this was useful to you <3
