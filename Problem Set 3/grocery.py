def main():
    groceryList = {}

    while True:
        try:
            item = input().strip().lower()
            if item:
                groceryList[item] = groceryList.get(item, 0) + 1
        except KeyError:
            pass
        except EOFError:
            print()
            break

    for item in sorted(groceryList):
        print(f"{groceryList[item]} {item.upper()}")

main()
