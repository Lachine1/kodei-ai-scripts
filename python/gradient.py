'''
This code will generate a random gradient image.
The code starts by importing the "random" and "math" modules, and the "Image" class from the "PIL" package.
The code then defines a function named "generate_random_color" that returns a random color.
The code then defines a function named "interpolate_color" that interpolates a color between 2 colors.
The code then defines a function named "generate_random_gradient" that generates a random gradient image.
The code then defines a function named "main" that prompts the user for width and height and then saves a gradient image.
'''
import random    # Import random module
import math    # Import math module
from PIL import Image    # Import image class from PIL package

def generate_random_color() -> tuple:
    """
    Generate random color.

    Returns
    -------
    tuple
        Random color (red, green, blue).

    """
    
    red = random.randint(0, 255)    # Generate a random integer between 0 and 255
    green = random.randint(0, 255)    # Generate a random integer between 0 and 255
    blue = random.randint(0, 255)    # Generate a random integer between 0 and 255
    return (red, green, blue)    # Return a tuple of random RGB value

def interpolate_color(color1: tuple, color2: tuple, factor: float = 0.5) -> tuple:
    """
    Interpolate color between two colors.

    Parameters
    ----------
    color1: tuple
        First color (red, green, blue).
    color2: tuple
        Second color (red, green, blue).
    factor: float, optional
        Factor of interpolation between two colors.

    Returns
    -------
    tuple
        Interpolated color (red, green, blue).

    """
    
    red = int(round(color1[0] + factor * (color2[0] - color1[0])))    # Interpolate value of red and round it to nearest integer
    green = int(round(color1[1] + factor * (color2[1] - color1[1])))    # Interpolate value of green and round it to nearest integer
    blue = int(round(color1[2] + factor * (color2[2] - color1[2])))    # Interpolate value of blue and round it to nearest integer
    return (red, green, blue)    # Return a tuple of interpolated RGB value

def generate_random_gradient(width: int, height: int) -> Image:
    """
    Generate Random Gradient Image.

    Parameters
    ----------
    width: int
        Width of Image.
    height: int
        Height of Image.

    Returns
    -------
    Image
        Random Gradient Image.

    """
    
    image = Image.new("RGB", (width, height))    # Initialize an image object of given width and height
    color1 = generate_random_color()    # Generate a random color
    color2 = generate_random_color()    # Generate a random color
    for y in range(height):    # Iterate over height
        for x in range(width):    # Iterate over width
            factor = x / width    # factor is equal to the horizontal position of pixel
            color = interpolate_color(color1, color2, factor)    # Get interpolated color
            image.putpixel((x, y), color)    # Set the interpolated color at given position
    return image    # Return the image object

def main() -> None:
    """
    Main Function.

    Returns
    -------
    None

    """
    
    width = int(input("Width: "))    # Take input from user
    height = int(input("Height: "))    # Take input from user
    image = generate_random_gradient(width, height)    # Initialize an image object
    image.save("gradient.png")    # Save the image object

if __name__ == "__main__":    # Check if the script is executed as main script
    main()    # Execute the main function
