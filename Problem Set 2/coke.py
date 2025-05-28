def main():
    denominations = [25, 10, 5]
    amountDue = 50

    while amountDue > 0:
        print(f"Amount Due: {amountDue}")
        userInput = int(input("Input Coin: ").strip().lower())

        for coin in denominations:
            if userInput == coin:
                amountDue -= coin
                break

    if amountDue < 0:
        amountDue = abs(amountDue)

    print(f"Change Owed: {amountDue}")

main()
