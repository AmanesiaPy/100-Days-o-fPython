import pandas
import datetime as dt
import random
import smtplib


MY_EMAIL = ""
PASSWORD = ""

data_to_send = None
to_send = False
# 1. Update the birthdays.csv
date_data = pandas.read_csv("birthdays.csv")
date_dictionary = date_data.to_dict(orient="records")
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
for data in date_dictionary:
    if now.day == data["day"] and now.month == data["month"]:
        data_to_send = data
        to_send = True
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if data_to_send:
    letter_number = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_number}.txt") as letter:
        to_send_letter = letter.read()
    letter_with_name = to_send_letter.replace("[NAME]", f"{data_to_send['name']}")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="",
                            msg=f"Subject:Happy Birthday\n\n{letter_with_name}"
                            )
# 4. Send the letter generated in step 3 to that person's email address.
