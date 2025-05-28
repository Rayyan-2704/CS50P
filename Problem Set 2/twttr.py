def main():
    userInput = input("Input: ").strip()
    print(f"Output: {twttr(userInput)}")

def twttr(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    newString = ""

    for char in str:
        if char in vowels:
            continue
        else:
            newString += char

    return newString

main()
