import smtplib

my_email = "codevizk@gmail.com"
password = "vydq ennv bbay ydau"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="vivek223singh@gmail.com",
                        msg="Subject:Hello\n\nFirst SMTP test.")
