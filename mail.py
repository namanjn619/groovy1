import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmailUser = 'sender'
gmailPassword = 'password'
recipient = 'recepient'

message = f'Website is not running.'

msg = MIMEMultipart()
msg['From'] = f'"Arjun" <{gmailUser}>'
msg['To'] = ''
msg['Subject'] = "Sending mail"
msg.attach(MIMEText(message))

try:
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmailUser, gmailPassword)
    mailServer.sendmail(gmailUser, recipient, msg.as_string())
    mailServer.close()
    print ('Email sent!')
except:
    print ('Something went wrong...')
~                                     