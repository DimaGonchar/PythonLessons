import smtplib
import ssl
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

receivers= open('receivers.txt','r')
cv="cv.docx"
port=465
sender='dmitriygonchar1997@gmail.com'
smtpServer=""
receiverEmail=""
password="@gonchar1997211"
smtpServers=[]
message = MIMEMultipart("alternative")
message["Subject"]="cv for a c ++ junior developer position"
message["From"]=sender
message["To"]=receiverEmail
with open('smtpServers.txt','r') as smtpServersFile:
    for smtp in smtpServersFile:
        smtpServers.append("smtp"+'.'+ smtp)
    
with open(cv,'rb') as attachment:
     part = MIMEText("application", "octet-stream")
     part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; cv= {cv}",
)

message.attach(part)
text = message.as_string()

#context = ssl.create_default_context()
#with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#   server.login(sender, password)
#    server.sendmail(
#        sender, receiverEmail, message.as_string()
#    )
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, "dmitriygonchar1997@gmail.com", text)