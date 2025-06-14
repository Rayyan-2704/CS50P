import inflect

def main():
    names = []

    while True:
        try:
            name = input("Name: ").strip()
            names.append(name)
        except EOFError:
            print()
            break

    p = inflect.engine()
    formattedNames = p.join(names)
    print(f"Adieu, adieu, to {formattedNames}")

main()
