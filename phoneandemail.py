#! python3

import pyperclip, re

# Create a RegEx for phone numbers

phoneRegex = re.compile(r'''
# 412-555-5555, 555-5555, (814) 555-5555, 555-5555 ext. 12345, etx. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?        #area code
(\s|-)        #first separator
\d\d\d        #first 3 digits
-        #separator
\d\d\d\d        #last 4 digits
(((ext(\.)?\s)|x)          #extension word-part
 (\d{2,5}))?                #extension number-part
)
''', re.VERBOSE)


# This line equates to the line above without using VERBOSE  -->    re.compile('((\d\d\d)|(\(\d\d\d\)))?(\s|-)\d\d\d-\d\d\d\d(((ext(\.)?\s)|x(\d{2,5}))?)


# TODO: create a RegEx for email adresses
emailRegex = re.compile(r'''


[a-dA-Z0-9_.+]+    #name part
@      # @ symbol
[a-dA-Z0-9_.+]+    # domain part


''', re.VERBOSE)



# TODO: get the text off the clipboard
text = pyperclip.paste()


                        
# TODO: extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)


allPhoneNumbers = []
for phoneNumber in extractedPhone:
        allPhoneNumbers.append(phoneNumber[0])
                   

#  for           print(extractedPhone)
#  test          print(extractedEmail)



# TODO: copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
