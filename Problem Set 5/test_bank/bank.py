def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    greeting = greeting.strip().lower()
    if "hello" in greeting:
        return 100
    elif greeting[0] == 'h':
        return 20
    else:
        return 0


if __name__ == "__main__":
    main()
