import time
from PIL import Image

# Load the original image
imgPath = r'K:\KevinStudies\CDU\Summer Semester\Software Now\PythonAssignment2\chapter1.jpg'
from PIL import Image
import time

# Load the original image
image_path = imgPath
original_image = Image.open(image_path)

# Get the generated number
current_time = int(time.time())
generated_number = (current_time % 100) + 50

# Get image dimensions
width, height = original_image.size

# Create a new image with the same mode and size
new_image = Image.new(original_image.mode, original_image.size)

# Update pixel values in the new image
for i in range(width):
    for j in range(height):
        r, g, b = original_image.getpixel((i, j))
        new_image.putpixel((i, j), (r + generated_number, g + generated_number, b + generated_number))

# Save the new image
output_path = r'K:\KevinStudies\CDU\Summer Semester\Software Now\PythonAssignment2\chapter1out.jpg'
new_image.save(output_path)

# Calculate and print the sum of red pixel values
red_pixel_sum = sum(new_image.getpixel((i, j))[0] for i in range(width) for j in range(height))
print("Sum of Red Pixel Values:", red_pixel_sum)