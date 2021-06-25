# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random


from twilio.rest import Client


today = datetime.now()
today_tuple = (today.month, today.day)

account_sid = "ACa5eabfd24b34a02cf051267d4b93bcd8"
auth_token = "b2e7209e9e38bd5010bcc99b1fac4480"


data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows( )}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read( )
        contents = contents.replace("[NAME]", birthday_person["name"])


        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                        body=f"{contents}.",
                        from_='+14085027967',
                        to='+250788740725'
        )



