from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import random


class ImgObject:
	def __init__(self, image, brightness=100, blur=0):
		self.image = image
		self.brightness = brightness
		self.blur = blur

	def __repr__(self):
		return f"ImgObject(image='{self.image}', brightness={self.brightness}, blur={self.blur})"


def GenerateColors():
	foreground_color = (
		random.randint(0, 255),
		random.randint(0, 255),
		random.randint(0, 255),
	)

	background_color = (
		random.randint(0, 255),
		random.randint(0, 255),
		random.randint(0, 255),
	)

	while abs(sum(foreground_color) - sum(background_color)) < (255 * 3) / 2:
		background_color = (
			random.randint(0, 255),
			random.randint(0, 255),
			random.randint(0, 255),
		)

	return foreground_color, background_color


def Convert(quote, author, fg, bg, font_type, font_size, width, height, watermark_text, watermark_font_size:int=None, font_size_author:int=None):
	if isinstance(bg, ImgObject):
		image = Image.open(bg.image).resize((width, height))
		enhancer = ImageEnhance.Brightness(image)
		image = enhancer.enhance(bg.brightness / 100)
		if bg.blur != 0:
			image = image.filter(ImageFilter.BoxBlur(bg.blur))
	else:
		image = Image.new("RGB", (width, height), bg)

	draw = ImageDraw.Draw(image)

	if font_size_author is None:
		font_size_author = font_size

	font = ImageFont.truetype(font_type, font_size)
	font_author = ImageFont.truetype(font_type, font_size_author)

	lines = []
	line = ""
	for word in quote.split():
		line_width = draw.textsize(line + " " + word, font)[0]
		if line_width > width-40:
			lines.append(line)
			line = word
		else:
			line += " " + word
	lines.append(line)

	quote_height = sum([draw.textsize(line, font)[1] for line in lines])
	y = (height - quote_height - font_size) // 2

	for line in lines:
		line_width = draw.textsize(line, font)[0]
		x = (width - line_width) // 2
		draw.text((x, y), line, fg, font=font)
		y += draw.textsize(line, font)[1]

	dash_width = draw.textsize(" - ", font)[0]
	x = (width - dash_width) // 2
	y += font_size // 2
	draw.text((x, y), " - ", fg, font=font)
	y += font_size // 2

	author_width = draw.textsize(author, font_author)[0]
	x = (width - author_width) // 2
	draw.text((x, y+15), author, fg, font=font_author)

	if watermark_text:
		if watermark_font_size is None:
			watermark_font_size = font_size
		watermark_font = ImageFont.truetype(font_type, watermark_font_size)
		watermark_width, watermark_height = draw.textsize(watermark_text, watermark_font)
		x = width - watermark_width - 10
		y = height - watermark_height - 10
		draw.text((x, y), watermark_text, fg, font=watermark_font)

	return image
