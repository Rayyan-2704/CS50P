def main():
    time = input("What time is it? ").strip()
    hour = convert(time)

    if 7.0 <= hour <= 8.0:
        print("breakfast time")
    elif 12.0 <= hour <= 13.0:
        print("lunch time")
    elif 18.0 <= hour <= 19.0:
        print("dinner time")

def convert(time):
    hours, mins = time.split(":")
    hours = float(hours)
    mins = float(mins)
    return hours + (mins/60)

if __name__ == "__main__":
    main()
