import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.models.RequestModel import RequestModel


class EmailService:
    def __init__(self, responses, request: RequestModel):
        self.request = request
        self.responses = responses

    def trigger_email(self):
        smtp_server = "smtp.gmail.com"
        sender_email = "testvaccineprovider@gmail.com"  # Enter your address
        receiver_email = self.request.email_id  # Enter receiver address
        password = #password
        msg = MIMEMultipart('alternative')

        html = '<html><body><p>Hi, I have the following alerts for you! <br> <br>'
        for response in self.responses:
            html += response.__str__() + '<br> <br>'

        msg['Subject'] = 'Vaccine is now available for your pincode: ' + self.request.pin_code + '!'
        msg['From'] = sender_email
        msg['To'] = receiver_email

        html += '</p></body></html>'
        part2 = MIMEText(html, 'html')
        msg.attach(part2)
        print(msg['subject'])

        smtp = smtplib.SMTP_SSL(smtp_server)
        smtp.login(sender_email, password)
        smtp.sendmail(sender_email, receiver_email, msg.as_string())
        smtp.quit()