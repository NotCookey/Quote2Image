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
