<h1 align="center">Quote2Image</h1>
<p align="center"><b>A python module to convert text quotes into graphical images</b></p>
<p align="center"><kbd><img src="https://github.com/NotCookey/Quote2Image/assets/88582190/c49bedbd-73a5-4eac-a1b0-a4d98445ae08" height=300px></kbd></p>

## Installation
**To install Quote2Image, you can use `pip`:**
```bash
pip install Quote2Image
```

## Usage
**The `Convert` function takes the following arguments:**

- **`quote` : The quote to convert.**
- **`author` : The author of the quote.**
- **`fg` : The foreground color of the text.**
- **`bg` : The background color of the image.**
- **`font_type` : The font to use for the text.**
- **`font_size` : This font size is used for the quote.**
- **`font_size_author` : This font size is used for the author (Optional, Default value is set to `font_size`).**
- **`width` : The width of the image.**
- **`height` : The height of the image.**
- **`watermark_text` : The text for the watermark (Leave it blank for no watermarks).**
- **`watermark_font_size` : The font size for the watermark text (Optional, Default save is set to `font_size`).**

## Generating an image using RGB background and foreground

**The package comes with a builtin `GenerateColors` function that generates a fg and bg color with the correct amount of luminosity and returns them in tuples.**

```python
from Quote2Image import Convert, GenerateColors

# Generate Fg and Bg Color
fg, bg = GenerateColors()

img=Convert(
	quote="Pooing keeps you healthy",
	author="Pee",
	fg=fg,
	bg=bg,
	font_size=32,
	font_type="arial.ttf",
	width=1080,
	height=450)

# Save The Image as a Png file
img.save("hello.png")
```
## Generating an image using a custom background image.

 **We can do that using the `ImgObject` that gives us alot of flexibility on how we want our background Image to be.**

**The `ImgObject` class takes the following arguments:**

- **`image` : The link to the background image (required).**
- **`brightness` : The brightness of the image (optional, default is 100).**
- **`blur` : The blur of the image (optional, default is 0).**

**You can then use the `ImgObject` instance as the bg argument in the convert function:**

```py
from Quote2Image import Convert, ImgObject

bg=ImgObject(image="IMAGE FILE LOCATION", brightness=80, blur=80)

img=Convert(
	quote="Pooing keeps you healthy",
	author="Pee",
	fg=(21, 21, 21),
	bg=bg,
	font_size=32,
	font_type="arial.ttf",
	width=1080,
	height=450)

# Save The Image as a Png file
img.save("hello.png")
```

## Adding a watermark:

- **`watermark_text` : The text for the watermark.**
- **`watermark_font_size` : The font size for the watermark text.**

```py
from Quote2Image import Convert, GenerateColors

# Generate Fg and Bg Color
fg, bg = GenerateColors()

img=Convert(
	quote="Pooing keeps you healthy",
	author="Pee",
	fg=fg,
	bg=bg,
	font_size=32,
	font_type="arial.ttf",
	font_size_author=25,
	width=1080,
	height=450,
    	watermark_text="@My.Watermark",
    	watermark_font_size=15
)

# Save The Image as a Png file
img.save("hello.png")
```

## Permissions

- **You are allowed to use, modify, and distribute the module.**
- **You are allowed to distribute modified versions of the module, as long as you follow the terms of the license.**

## Obligations

- **You must include a copy of the GPL-3.0 license with the module.**
- **You must provide a copy of the source code of the module, either along with the modified version of the module or through a written offer to provide the source code.**
- **You must provide a prominent notice stating that you have modified the module, and the date of the modification.**
- **If you distribute the module, you must do so under the terms of the GPL-3.0 license.**

## Star History

<a href="https://star-history.com/#NotCookey/Quote2Image&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=NotCookey/Quote2Image&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=NotCookey/Quote2Image&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=NotCookey/Quote2Image&type=Date" />
  </picture>
</a>

# That's It
> **Thank You! Hope this was useful to you <3**
