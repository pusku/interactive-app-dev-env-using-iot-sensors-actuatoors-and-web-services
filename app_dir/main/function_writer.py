def actuator_function_writer(function_name, tag):
    file = open("app_dir/main/generated_functions.py", "a+")
    code = """
def """ + function_name + """(motor_status):
    url = 'http://127.0.0.1:8000/api/actuators/'
    data = {
        "topic": '""" + tag + """',
        "value": motor_status,
        "time": "2019-01-24T13:35:24.246226Z",
        "name": "1"
        }
    response = requests.post(url, data=data)
    print(response.text)
"""
    file.write(code)
    file.close()


def sensor_function_writer(function_name, tag):
    file = open("app_dir/main/generated_functions.py", "a+")
    code = """
def """ + function_name + """():
    empty_list=[]
    sensor_tag = """ + tag + """
    data = requests.get("http://127.0.0.1:8000/api/sensors/").json()
    for i in data:
        if i['topic']==sensor_tag:
            empty_list.append(i)
    data = empty_list[-1]
    print(data)
    data = int(data['value'])
    return(data)
"""
    file.write(code)
    file.close()


def mailbox_function_writer(function_name, tag):
    file = open("app_dir/main/generated_functions.py", "a+")
    code = """
def """ + function_name + "_Read" + """(param):
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
    
def """ + function_name + "_Search" + """(param):
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
    
def """ + function_name + "_Label" + """():
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
                  
class auth_""" + function_name + """:
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

class send_email_""" + function_name + """:
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
    
def """ + function_name + "_Send" + """(param):
    SCOPES = 'https://mail.google.com/'
    CLIENT_SECRET_FILE = 'media/mailbox/credentials.json'
    APPLICATION_NAME = 'Gmail API Python Quickstart'
    authInst = auth_""" + function_name + """(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
    credentials = authInst.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    sendInst = send_email_""" + function_name + """(service)
    message = sendInst.create_message_with_attachment('test17291729@gmail.com','test17291729@gmail.com','Testing 123', param, 'media/image.jpg')
    sendInst.send_message('me',message)
    """
    file.write(code)

    file.close()


def api_function_writer(function_name, tag):
    file = open("app_dir/main/generated_functions.py", "a+")
    code = """
def """ + function_name + "_Post" + """(param):
    empty_list=[]
    sensor_tag = """ + tag + """
    data = requests.get("http://127.0.0.1:8000/api/sensors/").json()
    for i in data:
        if i['topic']==sensor_tag:
            empty_list.append(i)
    data = empty_list[-1]
    print(data)
    data = int(data['value'])
    return(data)
    
def """ + function_name + "_Get" + """():
    empty_list=[]
    sensor_tag = """ + tag + """
    data = requests.get("http://127.0.0.1:8000/api/sensors/").json()
    for i in data:
        if i['topic']==sensor_tag:
            empty_list.append(i)
    data = empty_list[-1]
    print(data)
    data = int(data['value'])
    return(data)

def """ + function_name + "_Search" + """(param):
    empty_list=[]
    sensor_tag = """ + tag + """
    data = requests.get("http://127.0.0.1:8000/api/sensors/").json()
    for i in data:
        if i['topic']==sensor_tag:
            empty_list.append(i)
    data = empty_list[-1]
    print(data)
    data = int(data['value'])
    return(data)
"""
    file.write(code)
    file.close()
