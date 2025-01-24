def main():
    statement = input()
    convert(statement)

def convert(line):
    line = line.replace(":)", "🙂").replace(":(", "🙁")
    print(line)

main()
