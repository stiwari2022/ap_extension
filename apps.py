# Adds a form, second route

from flask import Flask, render_template, request
import imaplib
import email
app = Flask(__name__)
# ^ import nessecary files, flask requires pip installation 

# Flask procedure to execute different programs
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summarize")
def summarize():
    # retrieve message
    final_messages = main()
    # determine if there is an error, if so divert to error page
    if len(final_messages) == 0:
        return render_template("error.html")
    # Summerizing procedure
    for i in range(len(final_messages)):
            final_messages[i] = "HAH"
    # Format message to be displayed
    final_messages = ' '.join(final_messages)
    global senders 
    senders = " ".join(senders)
    global subjects
    subjects = " ".join(subjects)


    return render_template("summarize.html",  message=final_messages, subject=subjects, sender=senders)
            

@app.route("/categorize")
   
def categorize():
    # retrieve message
    final_messages = main()
    # determine if there is an error, if so divert to error page
    if len(final_messages) == 0:
        return render_template("error.html")

    # format message for display
    final_messages = ' '.join(final_messages)
    catagories = tagMail(final_messages)

    global senders 
    senders = " ".join(senders)
    global subjects
    subjects = " ".join(subjects)
    
    

    return render_template("categorize.html", message=final_messages, subject=subjects, sender=senders, catagory = catagories)







def main():
    # Login credentials, requires manual input as of now
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
    
    # Make email contents ready for viewing 
    final_messages = printMail(msgs)
    return (final_messages)






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
    if len(mail_id_list) > 1:
        msgs = ["ERROR"]
    return msgs

def tagMail(plain_text):
        # Define key words to search for
        # --------------------------------INPUT CUSTOM WORDS------------------------------
        # Match the theme ["word", "word", "word"], in all lowercase
        # replace "WORD" with topic you want emails to fall in
        words1 = ["meeting", "business", "boss"]
        words2 = ["lol", "fr", "yo",]
        words3 = []
        words4 = []
        words5 = []
        # Convert to lower case for easy search
        plain_text.lower()
        textList = plain_text.split()
        # Search, if match found return topic
        for item in textList:
            if item in words1:
                return "Formal"
            elif item in words2:
                return "Informal"
            elif item in words3:
                return "WORD"
            elif item in words4:
                return "WORD"
            elif item in words5:
                return "WORD"
            else:
                return "None"
            
    

def printMail(msgs):
    # Print the message

    # Assign global variables to be transfered to main function                 
    global subjects
    subjects = []
    global senders 
    senders = []

    final_messages = []
    for msg in msgs[::-1]:
        for response_part in msg:
            if isinstance(response_part, tuple):
                my_msg = email.message_from_bytes(response_part[1])
                # print("_________________________________________")
                # print("subj:", my_msg['subject'])
                # print("from:", my_msg['from'])
                # print("body:")

                senders.append(my_msg['from'])

                subjects.append(my_msg["subject"])
                # subjects.append(my_msg["subject"])
                # What does this even mean???
                plain_text = ""
                html_text = ""
                for part in my_msg.walk():
                    if part.get_content_type() == 'text/plain':
                        plain_text = part.get_payload(decode=True).decode()
                    elif part.get_content_type() == 'text/html':
                        html_text = part.get_payload(decode=True).decode()
                if plain_text:
                    final_messages.append(plain_text)
                else:
                    final_messages.append(html_text)
    return(final_messages)
