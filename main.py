import random
import smtplib
import datetime as dt

my_email = "carduibot@gmail.com"
password = "ydffosgveywfvfrr"

now = dt.datetime.now()
day_of_the_week = now.weekday()

if day_of_the_week == 0:
    with open("quotes.txt") as quotes_file:
        lines = quotes_file.readlines()
        quote_of_the_day = random.choice(lines)
        print(quote_of_the_day)

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="vanessa@reteguin.com",
                            msg=f"Subject:Monday Motivation\n\n{quote_of_the_day}")
        connection.close()


