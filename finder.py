import PIL
import pyautogui
from PIL import ImageColor
import time


def rgb_to_hex(rgb):
    """Passed a tuple of integers, returns a string of their hex values."""
    return '%02x%02x%02x' % rgb


def hex_to_rgb(hex):
    """Passed a hex string, returns rgb values in a tuple."""
    return ImageColor.getcolor(hex, "RGB")


def display_menu():
    """Prints a menu."""
    print("\n1. Convert from rgb to hex")
    print("2. Convert from hex to rgb")
    print("3. Identify a colour based on mouse position")
    print("Q. Quit the program")


userchoice = ""
while userchoice.lower() != "q":
    display_menu()
    userchoice = input("Please select from one of the options above: ")
    if userchoice == "1":
        try:
            r_input = input("\nPlease enter the R value: ")
            g_input = input("\nPlease enter the B value: ")
            b_input = input("\nPlease enter the G value: ")

            rgb_tuple = (int(r_input), int(g_input), int(b_input))
            print("Hex value is " + rgb_to_hex(rgb_tuple))
        except ValueError:
            print("Please enter valid RGB values.")

    if userchoice == "2":
        user_str = input("\nPlease enter the hex code: ")
        try:
            if user_str[0] == "#":
                print("RGB Values are:")
                print(hex_to_rgb(user_str))
            else:
                hex_str = "#" + user_str
                print("RGB Values are:")
                print(hex_to_rgb(hex_str))

        except ValueError:
            print("Please enter a correct hex code.")

    if userchoice == "3":
        t = input("\nA timer of 5 seconds will count down once you click enter. Make sure your mouse cursor is hovering over the selected color at that point.")
        time.sleep(5)
        print("Timer started...\n")

        pixel = pyautogui.pixel(pyautogui.position()[0], pyautogui.position()[1])
        print("RGB Values: ")
        print(pixel)
        print("Hex code: " + rgb_to_hex(pixel) + "\n")
