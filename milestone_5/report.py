import csv
from datetime import datetime

def decorator(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        print(f"Report for {data["month"]} generated\n---Birthdays---")
        print(f"Total: {data["total_amount_of_birthdays"]}\nBy department: ")
        for department, count in data["birthdays_by_department"].items():
            print(f"- {department}: {count}")
        print(f"---Anniversaries---\nTotal: {data["total_amount_of_anniversaries"]}\nBy department: ")
        for department, count in data["anniversaries_by_department"].items():
            print(f"- {department}: {count}")

    return wrapper

@decorator
def generate_report() -> dict:
    month = input("Enter the month (with a capital letter): ")
    total_amount_of_birthdays = 0
    birthdays_by_department = {}
    total_amount_of_anniversaries = 0
    anniversaries_by_department = {}

    with open("database.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:

            birthday_month = datetime.strptime(row["date_of_birth"], "%B %d").strftime("%B")
            hiring_date = datetime.strptime(row["hiring_date"], "%Y-%m-%d")

            if hiring_date == datetime.now().date:
                continue

            anniversary_date = hiring_date.replace(year = datetime.now().year)
            anniversary_month = anniversary_date.strftime("%B")

            if month == birthday_month:
                total_amount_of_birthdays += 1
                if row["department"] in birthdays_by_department:
                    birthdays_by_department[row["department"]] += 1
                else:
                    birthdays_by_department[row["department"]] = 1

            elif month == anniversary_month:
                total_amount_of_anniversaries += 1
                if row["department"] in anniversaries_by_department:
                    anniversaries_by_department[row["department"]] += 1
                else:
                    anniversaries_by_department[row["department"]] = 1

    return {
        "month": month,
        "total_amount_of_birthdays": total_amount_of_birthdays,
        "birthdays_by_department": birthdays_by_department,
        "total_amount_of_anniversaries": total_amount_of_anniversaries,
        "anniversaries_by_department": anniversaries_by_department
    }

generate_report()