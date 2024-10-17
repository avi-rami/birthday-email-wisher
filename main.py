##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import smtplib
import random

password = "yoie xmvd ebsh juyd"
my_email = "pythontester93@gmail.com"
other_email = "pythontester2002@yahoo.com"

birthday_data = pd.read_csv("birthdays.csv")
# print(birthday_data)
today = dt.datetime.now()

for (index, row) in birthday_data.iterrows():
    if (row.month, row.day) == (today.month, today.day):
        # random_letter = "letter_" + str(random.randrange(1, 4)) + ".txt"
        with open(f"letter_templates/letter_{random.randint(1,4)}.txt") as letter:
            letter = letter.read()
            updated_letter = letter.replace("[NAME],",f"{str(row['name'])},")
            # print(updated_letter)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row.email,
                msg=f"Subject:Happy Birthday!\n\n{updated_letter}")