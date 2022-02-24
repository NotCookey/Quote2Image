<h1 align="center">Quote2Image</h1>
<p align="center"><b>A Python Library to Make Quote Images</b></p>
<p align="center"><kbd><img src="https://cdn.discordapp.com/attachments/905732238237368351/919180108181422120/quote.png" height=300px></kbd></p>

# How To Use?
- **Download The Latest Package From [Releases](https://github.com/SecretsX/Quote2Image/releases)**
- **Extract The Zip File And Place Every File In It To Your Current Code Folder**

<kbd><img src="https://media.discordapp.net/attachments/905732238237368351/919182699686662204/unknown.png"></kbd>

- **Code Instructions**
```python
from Quote2Image import convert

# Font Size Default to 32, Height and Width by default is 612
img=convert(
	quote="Pooing keeps you healthy",
	author="Pee",
	fg="white",
	image="background_img.jpg",
	border_color="black",
	font_size=32,
	font_file=None,
	width=1080,
	height=450)

# Save The Image as a Png file
img.save("quote.png")
```

# That's It!
> Thank You! Hope this was useful to you <3
