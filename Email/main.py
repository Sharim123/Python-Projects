import smtplib
from random import choice
import datetime as dt


#
#
# my_email = "pythonpython05@gmail.com"
# password = "dsxxystfddszfurc"
#
# with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="pythonpython@myyahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my email")




# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# day_of_birth = dt.datetime(year=2002, month=5, day=18)
# print(day_of_birth)


with open("quotes.txt", "r") as file:
    quotes = file.readlines()
    one_quote = choice(quotes)


now = dt.datetime.now()
day_of_week = now.weekday()


my_email = "pythonpython05@gmail.com"
password = "dsxxystfddszfurc"



with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    if day_of_week == 0:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="pythonpython@myyahoo.com",
                            msg=f"Subject:Hello\n\n{one_quote}")
