import smtplib
import random
import pandas
import datetime as dt


date = dt.datetime.now()
today = (date.month, date.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}


if today in birthday_dict:
    n = random.randint(1, 3)
    file_path = f"letter_templates/letter_{n}.txt"
    birthday_person = birthday_dict[today]
    with open(file_path, mode="r") as letter:
        content = letter.read()
        new_content = content.replace("[NAME]", birthday_person["name"])
    user = "codevizk@gmail.com"
    password = "vydq ennv bbay ydau"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user, password=password)
        connection.sendmail(from_addr=user,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday!!\n\n{new_content}")


# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



