#FLASK MAIL IS USING HERE BECAUSE SENDGRID IS NOT WORKING:
# importing libraries
from flask import
Flask
from flask_mail import Mail,
Messageapp = Flask( name )
mail = Mail(app) # instantiate the mail class
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] =
'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
# message object mapped to a particular URL ‘/’
@app.route("/")
def index():
msg = Message('Hello', sender ='yourId@gmail.com' ,recipients =
['receiver’sid@gmail.com'])
msg.body = 'Hello Flask message sent from FlaskMail'mail.send(msg)
return 'Sent'
if name == ' main ':
app.run(debug = True)