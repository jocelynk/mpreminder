This repo is checks the db regularly and send reminders to users about their meetings via Twilio text messaging. 

To run this script simply add the following cronjob to the server

*/1 * * * * python PATH_TO_FILE/reminder.py

NOTE: Twilio only allows the messages to be sent to verified numbers if we don't upgrade our account. 
