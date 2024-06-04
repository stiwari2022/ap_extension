Gmail Categorizer and Summerizer.
  Authors: Ben and Shantanu
INSTRUCTIONS FOR USE:

Setting up permissions and access:
1. Steps Shantanu will write
2. more
3. Go to Gmail settings and enable both variants of the star[special starring, need to decide variants]
4. Put the email address and code in the list.
5. my_credentials = ["your.address@gmail.com", "entire code"].

How to install flask:
1. SHANTANU WILL WRITE THIS

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

How To Run Code in Terminal(launch website):
1. Install Flask using pip, use Google for any troubleshooting issues
2. Cd into the folder
3. Run python -m flask --app apps --debug  run
   - "apps" is the Python file name
   - include debug for live reload for updating, otherwise it is not necessary
