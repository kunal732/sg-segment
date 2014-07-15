#################################
#                               #
# Geographic List Segmentation  #
# with SendGrid Event Webhook   #
#                               #
# Created by Kunal Batra 7.14.14#
#################################

from flask import Flask,request, jsonify
import requests
import os

app = Flask(__name__)


#Create a new list for segmented countries, this must be a blank new list. Assign that new list to the variable below
sgList = os.environ['list']
sgUser = os.environ['api_user']
sgPass = os.environ['api_key']

#################################################################################
def addEmail(email, country):
   print "now in addEmail function"
   payload = { "api_user": sgUser, "api_key": sgPass, "list":sgList, "data": '{ "email": "'+email+'","name":"sg", "location": "'+country+'"}' }
   res = requests.post('https://api.sendgrid.com/api/newsletter/lists/email/add.json',data=payload)
   print "just made post request to sendgrid"
   print payload
   print res.text

def getLocation(ip):
   geoUrl = "http://freegeoip.net/json/"+ip
   #print geoUrl
   r = requests.get(geoUrl)
   data = r.json()
   print r.text
   country = data['country_name']
   return country

@app.route ('/', methods = ['GET'])
def index():
   return "OK"

@app.route('/', methods = ['POST'])
def segList():
   json = request.json
   for event in json:
      for attribute, value in event.iteritems():
	if attribute == 'email':
           address = value
        if attribute =='ip':
           country = getLocation(value)
           addEmail(address,country)
           print address, country
   return "OK"

if __name__ == '__main__':
   app.debug = True
   app.run()
