import smtplib


@dataclass
class Messenger:
    username: str
    password: str
    conn: smtplib.SMTP = None

    def open_conn(self):
        # CREATE CONNECTION TO SMTP SERVICE
        self.conn = smtplib.SMTP("smtp.gmail.com", 587)
        self.conn.ehlo()
        self.conn.starttls()
        self.conn.ehlo
        self.conn.login(self.username, self.password)

    def send_email(self, msg: str, one_time=False):
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
