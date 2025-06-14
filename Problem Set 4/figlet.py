from pyfiglet import Figlet
import sys
import random

def main():
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        print("Invalid usage")
        sys.exit(1)
    elif len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            print("Invalid usage")
            sys.exit(1)

    if len(sys.argv) == 1:
        randomFont()
    elif len(sys.argv) == 3:
        specificFont(selectedFont = sys.argv[2])

def randomFont():
    figlet = Figlet()
    fonts = figlet.getFonts()

    randomizedFont = random.choice(fonts)
    figlet.setFont(font = randomizedFont)

    str = input("Input: ").strip()
    print(f"Output:\n{figlet.renderText(str)}")

def specificFont(selectedFont):
    figlet = Figlet()
    fonts = figlet.getFonts()

    if selectedFont in fonts:
        figlet.setFont(font = selectedFont)

        str = input("Input: ").strip()
        print(f"Output:\n{figlet.renderText(str)}")
    else:
        print("Invalid usage")
        sys.exit(1)

main()
