import imapclient
import smtplib

imap_server = 'imap.gmail.com'
smtp_server = 'smtp.gmail.com'
username = 'brayanmuhindimwangi@gmail.com'
password = 'Sicafew74855!'

imapobj = imapclient.IMAPClient(imap_server, ssl=True)
imapobj.login(username, password)

smtpobj = smtplib.SMTP(smtp_server, 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.login(username, password)