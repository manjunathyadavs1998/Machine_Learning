import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import logging

class EmailSender:
    def __init__(self, user, smtp_server, smtp_port=25):
        self.user = user
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def create_smtp_session(self):
        """Create and return a custom SMTP client session object."""
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.set_debuglevel(1)  # Enable debug output for the SMTP session
            server.ehlo()  # Say hello to the server (EHLO/HELO command)
            return server
        except Exception as e:
            logging.error("Failed to create SMTP session: {}".format(str(e)))
            return None

    def attach_file(self, msg, file_path):
        """Attach a file to the email message."""
        try:
            with open(file_path, "rb") as file:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(file_path)}")
                msg.attach(part)
        except Exception as e:
            logging.error(f"Failed to attach file {file_path}: {str(e)}")

    def send_email(self, to_address, subject, text='', files=None):
        from_address = '{}@3ds.com'.format(self.user)
        format_address = to_address.split(',')
        send_to = ','.join(format_address)

        # Create email
        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = send_to
        msg['Subject'] = subject
        msg.attach(MIMEText(text, 'plain'))

        # Attach log files if provided
        if files:
            for file_path in files:
                self.attach_file(msg, file_path)

        # Create SMTP session
        smtp_session = self.create_smtp_session()
        if smtp_session is None:
            return

        try:
            email_text = msg.as_string()
            smtp_session.sendmail(from_address, format_address, email_text)
            logging.debug("Email sent to {} from {}".format(format_address, from_address))
        except Exception as e:
            logging.error("Failed to send email: {}".format(str(e)))
        finally:
            smtp_session.quit()

# Example usage
if __name__ == "__main__":
    sender = EmailSender(user="Manjunatha.YADAV", smtp_server="gimli.ux.dsone.3ds.com", smtp_port=25)
    to_address = "Minal.BITNE@3ds.com,Manjunathyada.SRINIVASA@3ds.com"
    subject = "Custom SMTP Session Email"
    text = "To test Build replays through python automation"

    # Specify log files to attach
    log_files = ["mkmk.log", "mkrtv.log"]  # Add your log files here

    sender.send_email(to_address, subject, text, files=log_files)
