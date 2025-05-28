def main():
    userInput = input("camelCase: ").strip()
    print(f"snake_case: {snake_case(userInput)}")

def snake_case(str):
    newString = ""

    for char in str:
        if char.isupper():
            newString += "_" + char.lower()
        else:
            newString += char

    return newString

main()
