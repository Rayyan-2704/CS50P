def main():
    expression = input("Expression: ").strip()
    x, y, z = expression.split()

    if y == '+':
        answer = float(x) + float(z)
    elif y == '-':
        answer = float(x) - float(z)
    elif y == '*':
        answer = float(x) * float(z)
    else:
        answer = float(x) / float(z)

    print(f"{answer:.1f}")

main()
