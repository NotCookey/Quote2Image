from Quote2Image import auto_color, convert

# Automatically Generates a Perfect Match of Colors for Fore and Back
color=auto_color()

img=convert(quote="Pooing keeps you healthy",author="Pee",fg=color[0],bg=color[1])

# Save The Image as a Png file
img.save("quote.png")

# Everytime you run this code it will generate a quote.png file with a different background and foreground