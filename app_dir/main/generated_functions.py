from __future__ import print_function

from googleapiclient import errors
from httplib2 import Http
from oauth2client import file, client, tools
import requests
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import base64
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import mimetypes

try:
    import argparse

    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def temperature_checker():
    empty_list=[]
    sensor_tag = temperature_checker
    data = requests.get("http://127.0.0.1:8000/api/sensors/").json()
    for i in data:
        if i['topic']==sensor_tag:
            empty_list.append(i)
    data = empty_list[-1]
    print(data)
    data = int(data['value'])
    return(data)

def Test_Read(param):
    store = file.Storage('media/mailbox/token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('media/mailbox/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    results = service.users().messages().list(userId='me',labelIds = [param]).execute()
    messages = results.get('messages', [])
    if not messages:
        print ("No messages found.")
    else:
        print ("Message snippets:")
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            print(msg['snippet'])
    
def Test_Search(param):
    store = file.Storage('media/mailbox/token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('media/mailbox/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    results = service.users().messages().list(userId='me',labelIds = ['INBOX']).setQ(param).execute()
    messages = results.get('messages', [])
    if not messages:
        print ("No messages found.")
    else:
        print ("Message snippets:")
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            print(msg['snippet'])
    
def Test_Label():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'media/mailbox/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])
                  
class auth_Test:
    def __init__(self,SCOPES,CLIENT_SECRET_FILE, APPLICATION_NAME):
        self.SCOPES = SCOPES
        self.CLIENT_SECRET_FILE = CLIENT_SECRET_FILE
        self.APPLICATION_NAME = APPLICATION_NAME
    def get_credentials(self):
        cwd_dir = os.getcwd()
        print(cwd_dir)
        credential_dir = os.path.join(cwd_dir, '.media/mailbox/')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'credentials.json')
        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(self.CLIENT_SECRET_FILE, self.SCOPES)
            flow.user_agent = self.APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

class send_email_Test:
    def __init__(self,service):
        self.service = service
    def create_message(self,sender, to, subject, message_text):
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        return {'raw': base64.urlsafe_b64encode(message.as_bytes())}

    def create_message_with_attachment(self,
        sender, to, subject, message_text, file):
        message = MIMEMultipart()
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        msg = MIMEText(message_text)
        message.attach(msg)
        content_type, encoding = mimetypes.guess_type(file)
        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
        main_type, sub_type = content_type.split('/', 1)
        if main_type == 'text':
            fp = open(file, 'rb')
            msg = MIMEText(fp.read(), _subtype=sub_type)
            fp.close()
        elif main_type == 'image':
            fp = open(file, 'rb')
            msg = MIMEImage(fp.read(), _subtype=sub_type)
            fp.close()
        elif main_type == 'audio':
            fp = open(file, 'rb')
            msg = MIMEAudio(fp.read(), _subtype=sub_type)
            fp.close()
        else:
            fp = open(file, 'rb')
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(fp.read())
            fp.close()
        filename = os.path.basename(file)
        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        message.attach(msg)
    
        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    def send_message(self, user_id, message):
        try:
            message = (self.service.users().messages().send(userId=user_id, body=message).execute())
            print('Message Id: %s' % message['id'])
            return message
        except errors.HttpError as error:
            print('An error occurred: %s' % error)
    
def Test_Send(param):
    SCOPES = 'https://mail.google.com/'
    CLIENT_SECRET_FILE = 'media/mailbox/credentials.json'
    APPLICATION_NAME = 'Gmail API Python Quickstart'
    authInst = auth_Test(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
    credentials = authInst.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    sendInst = send_email_Test(service)
    message = sendInst.create_message_with_attachment('test17291729@gmail.com','test17291729@gmail.com','Testing 123', param, 'media/image.jpg')
    sendInst.send_message('me',message)
    
def FirstAPI_Post(param):
    empty_list=[]
    sensor_tag = FirstAPI
    data = requests.get("http://127.0.0.1:8000/api/sensors/").json()
    for i in data:
        if i['topic']==sensor_tag:
            empty_list.append(i)
    data = empty_list[-1]
    print(data)
    data = int(data['value'])
    return(data)
    
def FirstAPI_Get():
    empty_list=[]
    sensor_tag = FirstAPI
    data = requests.get("http://127.0.0.1:8000/api/sensors/").json()
    for i in data:
        if i['topic']==sensor_tag:
            empty_list.append(i)
    data = empty_list[-1]
    print(data)
    data = int(data['value'])
    return(data)

def FirstAPI_Search(param):
    empty_list=[]
    sensor_tag = FirstAPI
    data = requests.get("http://127.0.0.1:8000/api/sensors/").json()
    for i in data:
        if i['topic']==sensor_tag:
            empty_list.append(i)
    data = empty_list[-1]
    print(data)
    data = int(data['value'])
    return(data)
