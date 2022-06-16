import imapclient
import smtplib

imap_server = 'imap.gmail.com'
smtp_server = 'smtp.gmail.com'
username = '#'
password = '#'

imapobj = imapclient.IMAPClient(imap_server, ssl=True)
imapobj.login(username, password)

smtpobj = smtplib.SMTP(smtp_server, 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.login(username, password)

category = []
for i in range(len(UIDs)):
    label_dict = imapobj.get_gmail_labels(UIDs[i])
    label = label_dict[UIDs[i]]
    if 'Starred' in str(label):
        category.append('Starred')
    elif 'Important' in str(label):
        category.append('Important')
    elif len(label) == 0:
        category.append('Inbox')
    else:
        category.append('Custom Label')
