def main():
    while True:
        try:
            x_str, y_str = input("Fraction: ").split("/")
            x = int(x_str)
            y = int(y_str)
            if y == 0:
                raise ZeroDivisionError()
            elif x > y:
                raise ValueError()
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            break

    calculatePercentage(x, y)

def calculatePercentage(a, b):
    percentage = round((a / b) * 100)
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

main()
