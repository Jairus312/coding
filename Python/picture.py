# Reload the image
image = Image.open(image_path)

# Prepare to draw on the image
draw = ImageDraw.Draw(image)

# Choose a larger font size
font_size = 40
try:
    font = ImageFont.truetype("arial.ttf", font_size)  # Use Arial if available
except IOError:
    font = ImageFont.load_default()  # Fallback to default

# Define text position and color
text_x = 50  # Left side of the image
text_y = 50  # Near the top
text_color = "white"

# Define text content
verse_text = "John 3:16\nFor God so loved the world,\nthat he gave his only begotten Son,\nthat whosoever believeth in him\nshould not perish, but have everlasting life."

# Draw text (left-aligned)
draw.text((text_x, text_y), verse_text, font=font, fill=text_color)

# Save the modified image
edited_image_path = "/mnt/data/A_man_kneeling_with_large_John_3_16.png"
image.save(edited_image_path)

# Provide the edited image path
edited_image_path
