import os
import smtplib
from email.message import EmailMessage

# Step 1: Specify the folder where the pictures are saved
picture_folder = "/Users/abrahambenson/Desktop/picture_folder"

# Step 2: Compose email
recipient = "abrahambenson25@yahoo.com"
subject = "Picture Report"
body = "Please find attached the latest picture."

# Step 3: Find the latest picture in the folder
latest_picture = os.path.join(picture_folder, "clu_cti.jpeg")

# Step 4: Attach the latest picture to the email
attachment = latest_picture

# Step 5: Send email
msg = EmailMessage()
msg['From'] = 'abrahambenson90@gmail.com'
msg['To'] = recipient
msg['Subject'] = subject
msg.set_content(body)

with open(attachment, 'rb') as f:
    file_data = f.read()
    file_name = os.path.basename(attachment)
msg.add_attachment(file_data, maintype='image', subtype='jpeg', filename=file_name)

# Send the email
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login('abrahambenson90@gmail.com', 'nlqh atxa pgfp zjza')  # Provide your email and password here
    smtp.send_message(msg)