# Program to get user's birthday and calculate age in days

from datetime import datetime

birthday_input = input("Enter your birthday (YYYY-MM-DD): ")

birthday = datetime.strptime(birthday_input, "%Y-%m-%d").date()
today = datetime.today().date()

age_in_days = (today - birthday).days

print(f"You are {age_in_days} days old.")

