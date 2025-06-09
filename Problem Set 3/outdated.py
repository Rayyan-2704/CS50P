def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            userInput = input("Date: ").strip().title()

            if "/" in userInput:
                dateList = userInput.split("/")

                if len(dateList) != 3:
                    raise ValueError()

                month_str, day_str, year_str = dateList
                month = int(month_str)
                day = int(day_str)
                year = int(year_str)

            else:
                if not "," in userInput:
                     raise ValueError()

                dateList = userInput.replace(",", "").split(" ")

                if len(dateList) != 3:
                    raise ValueError()

                month_str, day_str, year_str = dateList
                month = months.index(month_str) + 1
                day = int(day_str)
                year = int(year_str)

            if not (1 <= month <= 12 and 1 <= day <= 31):
                    raise ValueError()

            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

        except ValueError:
             pass

main()
