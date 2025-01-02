import smtplib
import datetime as dt
import random
from data import my_email, password, host, port

today = dt.datetime.now()
weekday = today.weekday()

with open('quotes.txt') as quotes_file:
    all_quotes = quotes_file.readlines()
    random_quote = random.choice(all_quotes)

with smtplib.SMTP(host, port) as connection:
    connection.starttls()
    connection.login(my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f'Subject: Today\'s Motivation\n\n{random_quote}')