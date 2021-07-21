import PIL
import pyautogui
from PIL import ImageColor


def rgb_to_hex(rgb):
    """Passed a tuple of integers, returns a string of their hex values."""
    return '%02x%02x%02x' % rgb


def hex_to_rgb(hex):
    """Passed a hex string, returns rgb values in a tuple."""
    return ImageColor.getcolor(hex, "RGB")


def display_menu():
    """Prints a menu."""
    print("1. Convert from rgb to hex")
    print("2. Convert from hex to rgb")
    print("3. Identify a colour based on mouse position")
    print("Q. Quit the program")


userchoice = ""
while userchoice.lower() != "q":
    display_menu()
    userchoice = input("Please select from one of the options above: ")
    if userchoice == "1":
        r_input = input("\nPlease enter the R value: ")
        g_input = input("\nPlease enter the B value: ")
        b_input = input("\nPlease enter the G value: ")

        rgb_tuple = (int(r_input), int(g_input), int(b_input))
        print("Hex value is " + rgb_to_hex(rgb_tuple) + "\n")