import smtplib
import datetime as dt
import pandas
import random

letter_no = random.randint(1, 3)
PLACE_HOLDER = "[NAME]"

my_email = "bikkasanit@gmail.com"
password = "cxlpwfrprjycugwd"

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")


now = dt.datetime.now()
month = now.month
date = now.day

for i in range(len(data_dict)):
    if data_dict[i]["month"] == month and data_dict[i]["day"] == date:
        with open(f"letter_templates/letter_{letter_no}.txt") as birthday_letter:
            birthday_content = birthday_letter.read()
            birthday_content = birthday_content.replace(PLACE_HOLDER, data_dict[i]["name"])
        with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=data_dict[i]["email"], msg=f"subject: Birthday Wishes\n\n"
                                                                                        f"{birthday_content}")
