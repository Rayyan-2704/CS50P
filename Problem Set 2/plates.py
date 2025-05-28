def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not (s[0:2].isalpha()):
        return False

    if not (s.isalnum()):
        return False

    if not numericCheck(s):
        return False

    return True

def numericCheck(s):
    numberStart = False
    for char in s:
        if not (numberStart) and char == '0':
            return False

        if char.isdigit():
            numberStart = True

        if numberStart and not (char.isdigit()):
            return False

    return True

main()
