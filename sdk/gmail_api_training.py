# Importing os and pickle module in program
import base64
import os
import pickle

from bs4 import BeautifulSoup
# Creating utils for Gmail APIs
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# Importing libraries for encoding/decoding messages in base64
from base64 import urlsafe_b64encode
# Importing libraries for dealing with the attachment of MIME types in Gmail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from mimetypes import guess_type as guess_mime_type

# Request all access from Gmail APIs and project
SCOPES = ['https://mail.google.com/']
OurEmailID = 'andy.havr1988@gmail.com'  # giving our Gmail Id


# using a default function to authenticate Gmail APIs
def authenticate_gmail_apis():
    creds = None
    # Authorizing the Gmail APIs with tokens of pickles
    if os.path.exists("token.pickle"):  # using if else statement
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
            # If there are no valid credentials available in device, we will let the user sign in manually
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_481384250289-t3ob9spl2p37hn8j26okm18ji299pj5j.apps.googleusercontent.com.json',
                SCOPES)  # downloaded credential name
            creds = flow.run_local_server(port=0)  # running credentials
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build('Gmail', 'v1', credentials=creds)  # using Gmail to authenticate


# Get the Gmail API service by calling the function
ServicesGA = authenticate_gmail_apis()


def read_email(gmail_connection):
    global code
    service = gmail_connection
    result = service.users().messages().list(userId='me').execute()
    messages = result.get('messages')
    for msg in messages:
        # Get the message from its id
        txt = service.users().messages().get(userId='me', id=msg['id']).execute()

        # Use try-except to avoid any Errors
        try:
            # Get value of 'payload' from dictionary 'txt'
            payload = txt['payload']
            headers = payload['headers']

            # Look for Subject and Sender Email in the headers
            for d in headers:
                # if d['name'] == 'Subject':
                #     subject = d['test']
                if d['name'] == 'From' and "gavandre@gmail.com" in d['value']:
                    sender = d['value']

                    # The Body of the message is in Encrypted format. So, we have to decode it.
            # Get the data and decode it with base 64 decoder.
            parts = payload.get('parts')[0]
            data = parts['body']['data']
            data = data.replace("-", "+").replace("_", "/")
            decoded_data = base64.b64decode(data)

            # Now, the data obtained is in lxml. So, we will parse
            # it with BeautifulSoup library
            soup = BeautifulSoup(decoded_data, "lxml")
            body = str(soup.body())
            otp_code = [int(i) for i in body if i.isdigit()]
            code = "".join(str(x) for x in otp_code)
        except:
            pass
        return code


# Using a default funnction to add attachments in Mail
def AddAttachment(mail, NameofFile):
    content_type, encoding = guess_mime_type(NameofFile)
    if content_type is None or encoding is not None:  # defining none file type attachment
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':  # defining text file type attachment
        fp = open(NameofFile, 'rb')  # opening file
        msg = MIMEText(fp.read().decode(), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':  # defining image file type attachment
        fp = open(NameofFile, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'audio':  # defining audio file type attachment
        fp = open(NameofFile, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)  # reading file
        fp.close()
    else:
        fp = open(NameofFile, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()  # closing file
    NameofFile = os.path.basename(NameofFile)
    msg.add_header('Content-Disposition', 'attachment', NameofFile=NameofFile)
    mail.attach(msg)  # composing the mail with given attachment


# Creating mail with a default function
def CreateMail(RecieverMail, SubofMail, BodyofMail,
               attachments=[]):  # various import content of mail as function's parameter
    # Using if else to check if there is any attachment in mail or not
    if not attachments:  # no attachment is given in the mail
        mail = MIMEText(BodyofMail)  # Body of Mail
        mail['to'] = RecieverMail  # mail ID of Reciever
        mail['from'] = OurEmailID  # our mail ID
        mail['subject'] = SubofMail  # Subject of Mail
    else:  # attachment is given in the mail
        mail = MIMEMultipart()
        mail['to'] = RecieverMail
        mail['from'] = OurEmailID
        mail['subject'] = SubofMail
        mail.attach(MIMEText(BodyofMail))
        for NameofFile in attachments:
            AddAttachment(mail, NameofFile)
    return {'raw': urlsafe_b64encode(mail.as_bytes()).decode()}


# Creating a default function to send a mail
def SendMail(ServicesGA, RecieverMail, SubofMail, BodyofMail, attachments=[]):
    return ServicesGA.users().messages().send(
        userId="me",
        body=CreateMail(RecieverMail, SubofMail, BodyofMail, attachments)
    ).execute()  # Body of the mail with execute() function


# Sending an email by adding important content, i.e., Reciever's mail, Subject, Body, etc.
# SendMail(ServicesGA, "gavandre@gmail.com", "Test", "Test API", ["test.txt",
# "client_secret_481384250289-t3ob9spl2p37hn8j26okm18ji299pj5j.apps.googleusercontent.com.json"])
# calling out default SendMail() function

read_email(authenticate_gmail_apis())
