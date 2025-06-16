def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break

    print(gauge(percentage))


def convert(fraction):
    x_str, y_str = fraction.split("/")
    x = int(x_str)
    y = int(y_str)
    if y == 0:
        raise ZeroDivisionError()
    if x > y:
        raise ValueError()
    return str(round((x / y) * 100))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}"


if __name__ == "__main__":
    main()
