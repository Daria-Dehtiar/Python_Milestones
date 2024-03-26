from faker import Faker
from datetime import datetime
import random
import csv

fake = Faker()

fields = ["department", "name", "date_of_birth", "age", "hiring_date"]
departments = [
    "Human Resources",
    "Marketing",
    "Production Engineering",
    "Research and Development",
    "Design", "Administration",
    "Sales",
    "Distribution",
    "Finance",
    "Security"
]

with open('database.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames = fields, delimiter = ',')
    writer.writeheader()

    for _ in range(1000):
        profile = {}
        profile['department'] = random.choice(departments)
        profile['name'] = fake.name()
        birthdate_with_year = fake.date_of_birth()
        profile['date_of_birth'] = birthdate_with_year.strftime('%B %d')
        profile['age'] = random.randint(22, 45)
        hiring_date = fake.date_time_between_dates(datetime.strptime('2015-06-12', '%Y-%m-%d'), datetime.now())
        profile['hiring_date'] = hiring_date.strftime('%Y-%m-%d')

        writer.writerow(profile)