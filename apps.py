# Adds a form, second route

from flask import Flask, render_template, request
import imaplib
import email
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet")
# ^ import nessecary files, yaml requires pip installation
def main():
    # Open file with credentials and set it to a variable
    # f = open("credentials.csv", "r")
    # my_credentials = []
    # for row in f:
    #     my_credentials.append(row)
    # my_credentials = f
    my_credentials = ["benson.computer.project@gmail.com", "ztwf bpcw bsdq qfuo"]

    # Set variables for login
    user, password = my_credentials[0], my_credentials[1]

    # Specify what the imap is accessing(gmail)
    imap_url = 'imap.gmail.com'

    #Essentially opens a port in order to access url, Documentation: https://docs.python.org/3/library/imaplib.html
    my_mail = imaplib.IMAP4_SSL(imap_url)

    # Use port to login
    my_mail.login(user, password)

    # Use port to select a folder/label (in this case we're access the main inbox)
    my_mail.select('Inbox')

    # ----------------Set search parameters-----------------, use this if looking for something specific https://support.google.com/mail/answer/7190?hl=en
    key = 'X-GM-RAW'
    value = 'is:starred'
    msgs = searchMail(my_mail, key, value)
    
    final_messages = printMail(msgs)
    final_messages = ' '.join(final_messages)

    return render_template("greet.html", message=final_messages)



def searchMail(my_mail, key, value):
    # Search using parameters
    _, data = my_mail.search(None, key, value)
    # Assign flagged emails that match parameters to an id list.
    mail_id_list = data[0].split()
    msgs = []
    # Search for message contents within each email, '(RFC822)' is a standard signiture for digital mail, append it to msg
    for num in mail_id_list:
        typ, data = my_mail.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs


def tagMail(plain_text):
        textList = plain_text.split()
        for item in textList:
            if item == "the":
                return True


def printMail(msgs):
    # Print the message
    final_messages = []
    for msg in msgs[::-1]:
        for response_part in msg:
            if isinstance(response_part, tuple):
                my_msg = email.message_from_bytes(response_part[1])
                # print("_________________________________________")
                # print("subj:", my_msg['subject'])
                # print("from:", my_msg['from'])
                print("body:")
                # What does this even mean???
                plain_text = ""
                html_text = ""
                for part in my_msg.walk():
                    if part.get_content_type() == 'text/plain':
                        plain_text = part.get_payload(decode=True).decode()
                    elif part.get_content_type() == 'text/html':
                        html_text = part.get_payload(decode=True).decode()
                if tagMail(plain_text) == True:
                    print("check", "")

                if plain_text:
                    final_messages.append(plain_text +"\n")
                else:
                    final_messages.append(html_text + "\n")
    return(final_messages)
