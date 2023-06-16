import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Gmail SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create a message object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Create a secure connection with the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to the Gmail account
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(msg)

        print("Email sent successfully")
    except Exception as e:
        print("Error sending email:", str(e))
    finally:
        # Close the connection to the SMTP server
        server.quit()

# Example usage
sender_email = 'youremail@gmail.com'  # Enter your email address
sender_password = 'yourpassword'  # Enter your gmail app password
recipient_email = 'recipient@example.com'  # Enter the recipient's email address
subject = 'Hello from Python!'
message = 'Hi, this is an example of sending emails using Python.'

send_email(sender_email, sender_password, recipient_email, subject, message)
