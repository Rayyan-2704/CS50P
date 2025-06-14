from random import randint

while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            raise ValueError
        break
    except ValueError:
        pass

number = randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
