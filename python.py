from faker import Faker
from PIL import Image, ImageDraw, ImageFont

# Create a Faker instance
fake = Faker()

# Generate simulated handwritten text
simulated_handwriting = """your text goes here"""
# Set up image parameters
image_width = 1447
image_height = 1877
text_color = "black"
font_size = 52
line_height = 56  # Height of each line on the lined paper
top_margin = 183  # Top margin above the first line

# Load a lined paper background image
lined_paper_path = "assets/paper.jpeg"
lined_paper = Image.open(lined_paper_path)

# Create a blank image with lined paper background
image = Image.new("RGB", (image_width, image_height))
image.paste(lined_paper, (0, 0))

# Create a drawing object
draw = ImageDraw.Draw(image)

# Choose your custom handwriting font
font_path = "assets/your-font.ttf"
font = ImageFont.truetype(font_path, font_size)

# Set horizontal text position
x = 20

# Calculate the y-coordinate based on the top margin
y = top_margin

# Draw the simulated handwritten text on the image, considering line heights
lines = simulated_handwriting.split('\n')
for line in lines:
    words = line.split()
    current_line = ""
    for word in words:
        # Check if adding the word exceeds the width of the image
        if draw.textsize(current_line + word, font)[0] <= image_width - x - 20:  # Adjust 20 for padding
            current_line += word + " "
        else:
            # Move to the next line
            draw.text((x, y), current_line.strip(), font=font, fill=text_color)
            y += line_height
            current_line = word + " "

    # Draw the remaining part of the line
    draw.text((x, y), current_line.strip(), font=font, fill=text_color)
    y += line_height

# Save the image with lined paper background
output_image_path = "output/handwriting.png"
image.save(output_image_path)

print(f"Output image saved at: {output_image_path}")
