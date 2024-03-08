# AUTOMATING PICTURE REPORTS
Walking through a step by step guide on how to achive an automated email report using python3:

## Step 1, Importing Modules
The script starts by importing necessary modules:
* os: Provides functions for interacting with the operating system.
* smtplib: Allows sending emails using the Simple Mail Transfer Protocol (SMTP).
* EmailMessage: Represents an email message.

## Step 2, Specify Picture Folder and Email Details:
* picture_folder: This variable specifies the folder where the pictures are saved. You should * replace it with the actual path to your picture folder.
* recipient: Specifies the recipient's email address.
* subject: Specifies the subject of the email.
* body: Specifies the body of the email.

## Step 3, Find the Latest Picture in the Folder:
* It constructs the path to the latest picture file in the specified picture_folder.
* It uses os.listdir(picture_folder) to get a list of files in the folder and then os.path.getctime() to get the creation time of each file.
* Finally, it selects the file with the maximum creation time, which should be the latest picture.

## Step 4, Attach the Latest Picture to the Email:
* It sets the attachment variable to the path of the latest picture file.

## Step 5, Compose the Email:
* It creates an EmailMessage object to represent the email.
* It sets the sender, recipient, subject, and body of the email using the appropriate methods (msg['From'], msg['To'], msg['Subject'], msg.set_content()).

## Step 6, Attach the Picture to the Email:
* It reads the contents of the picture file (latest_picture) in binary mode.
* It adds the picture file as an attachment to the email using msg.add_attachment(). It specifies the file data, MIME type (image/jpeg), and filename.

## Step 7, Send the Email:
* It establishes a connection to the SMTP server (smtp.gmail.com on port 587) using smtplib.SMTP().
* It initiates TLS encryption using starttls() to secure the connection.
* It logs in to the SMTP server using the sender's email address (abrahambenson90@gmail.com) and password.
* It sends the email message using smtp.send_message().

### Author: Abraham Benson