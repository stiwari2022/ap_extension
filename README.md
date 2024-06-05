Gmail Categorizer and Summerizer.
  Authors: Ben and Shantanu
INSTRUCTIONS FOR USE:

Setting up permissions and access:
1. Go to gmail.com
2. Click the settings button on the top right of the page and then click See All Settings
3. From there, you should be in a tab called General, and click on the tab, Forwarding and POP/IMAP.
4. Near the bottom of that page, change the setting to Enable IMAP, and then click Save Changes
5. Then go to this link, myaccount.google.com/u/2/signinoptions/twosv, and turn on two step verification
6. Then go to, myaccount.google.com/u/2/apppasswords, and create an app password
7. Make sure you record the app password eventhough it tells you not to
10. Go to Gmail settings and enable both variants of the star[special starring, need to decide variants]
11. Put the email address and code in the list
12. Go to the code and find the variable my_credentials, and replace that whole line with, my_credentials = ["your.address@gmail.com", "app password"]

How to install flask and other libraries:
1. Open your terminal
2. Copy this into it, pip install Flask
3. If that doesn't work, run pip3 install Flask
4. Run, pip install python-imap, or pip3 install python-imap
5. Then run, pip install email, or pip3 install email

To Categorize:
1. Ensure the emails you want to be sorted are specially starred.
2. Do this by clicking on the star option when hovering over the emails.
3. Click Categorize
4. The website display box will now display the email's sender, subject, and body. It will also display what category it has been assigned to.
5. If no category can be found the default value will be displayed as "none"

How to implement custom keywords and topics
1. Go to line 114
2. Per each word list, write down custom words
3. Match the theme ["searchword", "searchword", "searchword"], in all lowercase, these are the words you want to be flagged.
4. replace "WORD" with the topic you want emails to fall in 

To Summarize:
1. Ensure the emails you want to be sorted are specially starred.
2. Do this by clicking on the star option when hovering over the email.
3. Click Summarize
4. The summarization of the emails will be displayed in the display box along with the sender, and subject. The summarization will take place instead of the body.

CODE REFERENCES:
Explanation of code can be found in the actual code files.

How To Run Code in Terminal (launch website):
1. Install Flask using pip, use Google for any troubleshooting issues
2. Cd into the folder
3. Run python -m flask --app apps --debug  run
   - "apps.py" is the Python file name
   - Include debug for live reload for updating, otherwise it is not necessary
   - You should see a part that you copy and paste into the search bar of whatever browser you use
