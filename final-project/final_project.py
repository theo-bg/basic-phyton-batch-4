# https://realpython.com/python-send-email/
# https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/
# https://www.tutorialspoint.com/send-mail-from-your-gmail-account-using-python

import smtplib                                  #module for sending emails
from email import encoders                      #for encode payloads
from email.mime.multipart import MIMEMultipart  #to create multipart message object 
from email.mime.text import MIMEText            #to create the plain text attachments
from email.mime.base import MIMEBase            #to create base to other subclasses
import getpass
import stdiomask

print("----------------------")
print("SEND EMAIL WITH PYTHON")
print("----------------------")

#LOGIN
print("Sign in to your Gmail account")
sender_address = input("Enter your email               : ")
while True:
    sender_pass = stdiomask.getpass("Enter your password            : ")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)    #connect to host and port 
        server.starttls()                               #for encryption / secure connection
        server.login(sender_address, sender_pass)       #for login to gmail
        print ("\nLOGIN SUCCESS")
        break
    except smtplib.SMTPAuthenticationError:             #SMTP exception
        print("Wrong Username/Password.")

print("\nCompose New Message")

r = open("receiver_list.txt","r")

receiver_list = []

temp= r.readlines()
for i in temp:
    receiver_list.append(i.strip())
r.close()

#Input Email Subject
subject = input("Enter your subject (required)  : ")
while len(subject) == 0:
    subject = input("Enter your subject (required)  : ")

#Input Text in Body
text_body = input("Enter your message             : ")

#Input Attachment
add_atch = input("Add Attachment? (Y/N)          : ")

#Setup the MIME
msg = MIMEMultipart()

#Choose Attachment

if add_atch == "Y":
    atch_file= input("Attachment (1 file)            : ")   #input attachment with the file type ex: file_test.txt
    # Open file in binary mode
    attachment = open(atch_file,"rb") 
    # Add file as application/octet-stream
    part = MIMEBase('application', 'octet-stream') 
    # To change the payload into encoded form
    part.set_payload((attachment).read()) 
    # Encode file to base64 
    encoders.encode_base64(part) 
    # Add header as key/value pair to attachment part
    part.add_header('Content-Disposition', "attachment; filename= %s" % atch_file) 
    msg.attach(part)
else:
    print()

for z in receiver_list:
    # Create a multipart message and set headers
    msg['From'] = sender_address
    msg['To'] = z
    msg['Subject'] = subject
    body = text_body + "\n\nThis email is send by python"

    #The body attachments for the mail
    msg.attach(MIMEText(body, 'plain'))

    #Converts the Multipart msg into a string
    text = msg.as_string()

# sending the mail
server.sendmail(sender_address, receiver_list, text)

# terminating the session
server.quit()

print("\nMESSAGE SENT")
print("------------")