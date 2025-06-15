import random

levels = [1, 2, 3]

def main():
    score = 0
    level = get_level()

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        correct = False
        for j in range(3):
            try:
                userInput = int(input(f"{x} + {y} = ").strip())

                if userInput != (x + y):
                    raise ValueError()

            except ValueError:
                print("EEE")
                pass

            else:
                score = score + 1
                correct = True
                break

        if not correct:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())

            if level in levels:
                return level

            else:
                raise ValueError()

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
