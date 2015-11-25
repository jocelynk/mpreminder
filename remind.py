## Connects to db to check for meeting times
import pymongo

from pymongo import MongoClient
client = MongoClient()
client = MongoClient('mongodb://halilakin:heroku_p43wgxfq@ds035014.mongolab.com:35014/heroku_p43wgxfq')
db = client['heroku_p43wgxfq']


## Twilio SMS Api

from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC98e72a8adba88ca97ef68ba29a0e58a6"
auth_token = "cf6a808ac4430fa89c6bcd46ca4fccce"
# our valid phone number associated with these credentials +1 650-399-9202

client = TwilioRestClient(account_sid, auth_token)


# Example Call
# message = client.messages.create(to="+12316851234", from_="+15555555555",
#                                     body="Hello there!")

meetings = db.meetings

def isInAnHour(time):
    import dateutil.parser
    meetingTime = dateutil.parser.parse(time)
    inMinutes = (meetingTime.replace(tzinfo=None)-datetime.now()).days * 24 * 60
    if inMinutes >55 and inMinutes < 65:
        return 1
    return 0

# We gotta put money to our Twilio account, otherwise it only allows us to send message to verified numbers
for meeting in meetings.find():
    if not isInAnHour(meeting['date']):
        client.messages.create(to=str(meeting['phoneNumber']), from_="+16503999202",body="You have a meeting in an hour!")