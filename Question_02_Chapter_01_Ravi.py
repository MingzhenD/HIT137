import time
from PIL import Image

INPUT_IMAGE_PATH = 'chapter1.jpg'
OUTPUT_IMAGE_PATH = 'chapter1out.png'

current_time = int(time.time())

generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

print(generated_number)

def change_rgb(image_path, output_path, new_value_to_add):
    # Open the image
    image = Image.open(image_path)

    # Get the size of the image
    width, height = image.size

    # Create a new image with the same size and RGB mode
    new_image = Image.new("RGB", (width, height))

    # Iterate through each pixel in the original image
    print('Processing image...')
    for x in range(width):
        for y in range(height):            
            # Get the RGB values of the pixel
            old_red, old_green, old_blue = image.getpixel((x, y))

            # Change the RGB values based on your requirements
            new_red_value = min(255, old_red + new_value_to_add)
            new_green_value = min(255, old_green + new_value_to_add)
            new_blue_value = min(255, old_blue + new_value_to_add)

            # Set the new RGB values for the pixel in the new image
            new_image.putpixel((x, y), (new_red_value, new_green_value, new_blue_value))

    # Save the new image
    new_image.save(output_path)
    sum_all_red_values(output_path)

def sum_all_red_values(image_path):
    # Open the image
    image = Image.open(image_path)

    # Get the size of the image
    width, height = image.size

    # Initialize sum of red values
    red_sum = 0

    # Iterate through each pixel in the image
    for x in range(width):
        for y in range(height):
            # Get the RGB values of the pixel
            red_value, _, _ = image.getpixel((x, y))

            # Add the red value to the sum
            red_sum += red_value

    print('Sum: ' + str(red_sum))

#Method calling
change_rgb(INPUT_IMAGE_PATH, OUTPUT_IMAGE_PATH, generated_number)
print('Task completed')