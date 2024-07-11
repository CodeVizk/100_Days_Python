import smtplib

my_email = "YOUR MAIL@gmail.com"
password = "YOUR APP PASSWORD"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="RECEIVER@gmail.com",
                        msg="Subject:Hello\n\nFirst SMTP test.")
