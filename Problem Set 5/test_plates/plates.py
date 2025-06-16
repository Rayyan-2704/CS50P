def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (s[0:2].isalpha()):
        return False

    if not (s.isalnum()):
        return False

    numberStart = False
    for char in s:
        if not (numberStart) and char == '0':
            return False

        if char.isdigit():
            numberStart = True

        if numberStart and not (char.isdigit()):
            return False

    return True


if __name__ == "__main__":
    main()
