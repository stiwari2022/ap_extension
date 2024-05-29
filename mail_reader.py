import imaplib
import email
import yaml
# ^ import nessecary files, yaml requires pip installation
def main():
    # Open file with credentials and set it to a variable
    with open("credentials.yml") as f:
        my_credentials = yaml.safe_load(f)

    # Set variables for login
    user, password = my_credentials["user"], my_credentials["password"]

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
    printMail(msgs)

    
def searchMail(my_mail, key, value):
    # Search using parameters
    _, data = my_mail.search(None, key, value)
    # Assign flagged emails that match parameters to an id list.
    mail_id_list = data[0].split()
    print(mail_id_list)
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
                    print(plain_text)
                else:
                    print(html_text)


main()
