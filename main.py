import datetime as dt
import pandas as pd
import random
import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import base64

load_dotenv()

# Load email credentials from environment variables
MY_EMAIL = os.getenv('MY_EMAIL')


def authenticate_gmail():
    SCOPES = ['https://mail.google.com/']
    creds = None

    # Load token if it exists
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

    return creds.token

def send_letter(name, email):
    """Generate and send a birthday letter with an optional image attachment."""
    number = random.randint(1, 3)
    letter_path = f"letter_templates/letter_{number}.txt"

    # Read and personalize the letter
    with open(letter_path, "r") as file:
        letter_content = file.read().replace("[Name]", name)

    # Write the personalized message to a file
    with open("Letter_Templates/main_letter.txt", "w") as file:
        file.write(letter_content)

    # Create an EmailMessage object
    msg = EmailMessage()
    msg['Subject'] = f"Happy Birthday {name}!"
    msg['From'] = MY_EMAIL
    msg['To'] = email
    msg.set_content(letter_content)

    # Attach an image if it exists
    filepath = f"Images/Image_{number}.jpg"
    try:
        with open(filepath, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(filepath)
            msg.add_attachment(file_data, maintype='image', subtype='jpeg', filename=file_name)
    except FileNotFoundError:
        print(f"Attachment file not found: {filepath}")

    access_token = authenticate_gmail()
    auth_string = f"user={MY_EMAIL}\1auth=Bearer {access_token}\1\1"
    auth_string = base64.b64encode(auth_string.encode()).decode()

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.docmd("AUTH", "XOAUTH2 " + auth_string)
        smtp.send_message(msg)


# Get current day and month
now = dt.datetime.now()
day = now.day
month = now.month
present = f"{day}.{month}"

# Load birthday data
import requests

# Share the file and get a "raw" link
import requests

# Download CSV from Google Drive first
url = "https://drive.google.com/uc?export=download&id=1-gyJsKY3JjmhzsEp4CpGT2NSnl2PXXNs"
response = requests.get(url)
with open("Computer_Engineering_Datasheet.csv", "wb") as f:
    f.write(response.content)

# THEN load the birthdays
birthdays = pd.read_csv("Computer_Engineering_Datasheet.csv").to_dict(orient="records")
# Check if today is anyone's birthday√
for person in birthdays:
    if pd.notna(person.get('day')) and pd.notna(person.get('month')):
        if f"{int(person['day'])}.{int(person['month'])}" == present:
            name = str(person.get('Name')).strip()
            email = str(person.get('Email')).strip()
            if name and email and name.upper() != "N/A" and email.upper() != "N/A":
                send_letter(name, email)
