from twilio.rest import Client


account_sid = "ACa5eabfd24b34a02cf051267d4b93bcd8"
auth_token = "b2e7209e9e38bd5010bcc99b1fac4480"

client = Client(account_sid, auth_token)

client.messages.create(
        body="Happy birthday Athos White",
        from_='+14085027967',
        to='+250788740725'
        )