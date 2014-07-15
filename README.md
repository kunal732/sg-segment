## SendGrid Geo List Segmenation tool

This is a simple python application that takes advantage of SendGrid's
event webhook to segment your list by countries. .

###Install/Setup
1. Start by creating a new list in the SendGrid Marketing dashboard. This list will be used to store your new segmented emails. 
2. Make sure the Event Notification and Open Tracking apps are enabled. You can check by logging in and clicking on the Apps link in the header. 
3. Next Clone this repository and type the instructions below in the command line. 

```html
$ heroku create
$ heroku config:set list="NewList" #This is the new list you created in the SendGrid marketing Dashboard
$ heroku config:set api_user="YourUsername" #SendGrid account username
$ heroku config:set api_key="YourPass" #SendGrid account password
```
4. Make sure to deploy your app and get the url your app is deployed on. If you don't remember type in heroku info.
5. Enter that URL in the Event Notifications app settings and make sure "opened" is checked. 


Now you can send out an email campaign and your new list should be populated with the locations of your recipients. 

##License##

MIT

**Email kunal@sendgrid.com for any bugs.**

