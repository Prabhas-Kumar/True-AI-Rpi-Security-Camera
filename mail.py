import cv2
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

# Email you want to send the update from (only works with gmail)
fromEmail = 'email@gmail.com'
# You can generate an app password here to avoid storing your password in plain text
# https://support.google.com/accounts/answer/185833?hl=en
fromEmailPassword = 'password'

# Email you want to send the update to
toEmail = 'email2@gmail.com'

i = 0

def Send(image):
	cv2.imread(image)
	cv2.imwrite('detected'+str(i).jpg, image)
	filee='detected'+str(i)+".jpg"
	
	#create message object instance
	msg = MIMEMultipart()
	 
	 
	# setup the parameters of the message
	password = fromEmailPassword
	msg['From'] = fromEmail
	msg['To'] = toEmail
	msg['Subject'] = "Security update by Rpi. AI Cam!"
	
	msg.attach(MIMEImage(file(fille).read()))
	 
	 
	# create server
	server = smtplib.SMTP('smtp.gmail.com: 587')
	 
	server.starttls()
	 
	# Login Credentials for sending the mail
	server.login(msg['From'], password)
 
 
	# send the message via the server.
	server.sendmail(msg['From'], msg['To'], msg.as_string())
 
	server.quit()
 
	print "successfully sent email to %s:" % (msg['To'])
	
	i+=1
	
