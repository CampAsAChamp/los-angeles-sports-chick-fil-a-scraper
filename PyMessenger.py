'''
    Python Messaging package using the built in SMTP library.
    
    Features:
        - Email
            - HTML
            - Plain Text
        - SMS
        - Sends through your Gmail account
            NOTE: gmail account must have 'Less Secure APP Access' enabled.
                  Set this in your acount security settings.
                  
    Overview of provided message types:
        1. Email
            - to: example@example.com (String)
            - subject: (String)
            - body: (String) -> Can be in HTML format
            - is_HTML: defaults to False -> set True if body is in HTML format
        2. SMS
            - number: '12222222222' (String) -> include country code and area code
            - gateway: @txt.att.net (String) -> the SMS Gateway for the number
                - Look at the provider of recipient to select gateway
            - subject: (String)
            - body: (String)
            - recipient: DO NOT SET (auto created -> String)
    Overview of Messenger:
        - username: (String)
        - password: (String)
        Provided Functions: -> Example usage below
            - open_conn()
            - close_conn()
            - send_txt(msg, one_time=False)
            - send_email(msg, one_time=False)
            
    EXAMPLES:
    ----------------------------------------------------------------------------
    Example usage (one_time): -> cleaner code if sending one message
        my_messenger = Messenger(<your gmail username>, <your gmail password>)
        msg = SMS(number, gateway, subject, body)
        my_messenger.send_sms(msg, one_time=True)
        msg = Email(to, subject, body)
        my_messenger.send_email(msg, one_time=True)
    Example usage (not one_time): -> faster for sending lots of messages
        my_messenger = Messenger(<your gmail username>, <your gmail password>)
        my_messenger.open_conn()
        # send as many messages as you want here
        msg = SMS(number, gateway, subject, body)
        my_messenger.send_sms(msg)
        msg = Email(to, subject, body)
        my_messenger.send_email(msg)
        my_messenger.close_conn()
        
    SMS GATEWAYS
    ----------------------------------------------------------------------------
    AT&T: [number]@txt.att.net
    Sprint: [number]@messaging.sprintpcs.com or [number]@pm .sprint.com
    T-Mobile: [number]@tmomail.net
    Verizon: [number]@vtext.com
    Boost Mobile: [number]@myboostmobile.com
    Cricket: [number]@sms.mycricket.com
    Metro PCS: [number]@mymetropcs.com
    Tracfone: [number]@mmst5.tracfone.com
    U.S. Cellular: [number]@email.uscc.net
    Virgin Mobile: [number]@vmobl.com
    
    SMTP server names (You need to update line 123 to change this)
    ----------------------------------------------------------------------------
    Gmail                        smtp.gmail.com
    Outlook.com/Hotmail.com      smtp-mail.outlook.com
    Yahoo Mail                   smtp.mail.yahoo.com
    AT&T                         smpt.mail.att.net (port 465)
    Comcast                      smtp.comcast.net
    Verizon                      smtp.verizon.net (port 465)
'''
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dataclasses import dataclass

'''
    Message Types
'''
@dataclass
class Email:
    to: str
    subject: str
    body: str
    is_HTML: bool = False

@dataclass
class SMS:
    number: str
    gateway: str
    subject: str
    body: str
    @property
    def recipient(self) -> str:
        return self.number + self.gateway


'''
    Messager
'''
@dataclass
class Messenger:
    username: str # ALSO THE FROM ADDRESS
    password: str
    conn: smtplib.SMTP = None

    def open_conn(self):
        # CREATE CONNECTION TO SMTP SERVICE
        self.conn = smtplib.SMTP("smtp.gmail.com",587)
        self.conn.ehlo()
        self.conn.starttls()
        self.conn.ehlo
        self.conn.login(self.username, self.password)

    def close_conn(self):
        # CLOSE CONNECTION TO SMTP SERVICE
        self.conn.close()

    def send_sms(self, msg, one_time=False):
        if one_time:
            self.open_conn()

        # CREATE MESSAGE
        message = MIMEMultipart("alternative")
        message["From"] = self.username
        message["To"] =  msg.recipient
        message["Subject"] = msg.subject
        message.attach(MIMEText(msg.body, "plain"))
        # SEND MESSAGE
        self.conn.sendmail(self.username, msg.recipient, message.as_string())

        if one_time:
            self.close_conn()

    def send_email(self, msg, one_time=False):
        if one_time:
            self.open_conn()

        # CREATE MESSAGE
        message = MIMEMultipart("alternative")
        message["From"] = self.username
        message["To"] = msg.to
        message["Subject"] = msg.subject
        if msg.is_HTML:
            message.attach(MIMEText(msg.body, "html"))
        else:
            message.attach(MIMEText(msg.body, "plain"))
        # SEND MESSAGE
        self.conn.sendmail(self.username, msg.to, message.as_string())

        if one_time:
            self.close_conn()
