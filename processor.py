from datetime import datetime

# 1. Just for email:
import smtplib
from email.message import EmailMessage

def handle_webhook_event(payload):
    """
    This is your main webhook processor.
    Right now it's just a proof of concept.
    """

    print("\n===== PROCESSOR TRIGGERED =====")
    print("Time:", datetime.now())

    # Print the payload received from Planning Center
    print("Payload received:")
    print(payload)

    print("===== END PROCESSOR =====\n")


############### EMAIL SECTION ######################

# 2. Create the email message
msg = EmailMessage()
msg["Subject"] = "Script Notification"
msg["From"] = "rdean@itownchurch.com"
msg["To"] = "rdean@itownchurch.com"
msg.set_content("Hello, Your PCO webhook kicked off your python script.")

# 3. Connect to the server and send it
try:
    # This example uses Gmail's SMTP server configuration
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Upgrade the connection to secure
        server.login("rdean@itownchurch.com", "ugsl ovll mydp nckr") # If running from Google Cloud, place these in a password protector.
        server.send_message(msg)
    print("Email notification sent successfully!")
except Exception as e:
    print(f"Failed to send email. Error: {e}")

####################################################