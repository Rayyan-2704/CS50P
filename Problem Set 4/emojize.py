import emoji

def main():
    str = input("Input: ").strip()
    print(f"Output: {emoji.emojize(str, language = 'alias')}")

main()
