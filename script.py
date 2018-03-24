import requests
import time
import os
WEBHOSE_API_KEY = os.environ['WBAPK']
TWILIO_USER = os.environ['T_USER']
TWILIO_PASSWORD = os.environ['T_PASS']
TWILIO_KEY = os.environ['T_KEY']
TPHONE1 = os.environ['TPHONE1']
TPHONE2 = os.environ['TPHONE2']

news = requests.get("http://webhose.io/filterWebContent?token=" + WEBHOSE_API_KEY + "&format=json&ts=" + str(int(time.time() - 1800)) + "&q=language%3Aenglish(site_type%3Anews)&latest=true").json()['posts']

first = news[0]

resp = requests.post("https://" + TWILIO_USER + ":" + TWILO_PASSWORD + "@api.twilio.com/2010-04-01/Accounts/" + TWILIO_KEY + "/Messages.json", {'To':TPHONE1,'From':TPHONE2,'Body':first['title'] + ' - ' + first['thread']['site_section']})

