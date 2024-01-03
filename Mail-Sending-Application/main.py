import pandas as pd
import smtplib

your_email = "my_mail@ZZmail.com"
your_password = "pass"
'''
# establishing connection with gmail
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(your_email, your_password)
'''
# reading the spreadsheet
email_list = pd.read_excel('tigit.xlsx')

names = email_list['NAME']
emails = email_list['EMAILS']

# iterate through the records
for i in range(len(emails)):
    # for every record get the name and the email addresses
    name = names[i]
    email = emails[i]

    # the message to be emailed
    message = "Hello " + name
    # sending the email
    print(f"Gonderen:{your_email} \n Alici: {email} \n Message: {message} \n\n")

'''    
     server.sendmail(your_email, [email], message)
# close the smtp server
server.close()
'''
