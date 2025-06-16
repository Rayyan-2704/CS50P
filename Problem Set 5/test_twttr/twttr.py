def main():
    userInput = input("Input: ").strip()
    print(f"Output: {shorten(userInput)}")

def shorten(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    newWord = ""

    for char in word:
        if char in vowels:
            continue
        else:
            newWord += char

    return newWord


if __name__ == "__main__":
    main()
