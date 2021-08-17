import imaplib
import pprint
import cred

import imapclient
import smtplib
from cred import uname, pwd, imap, smtp

imap_server = imap
smtp_server = smtp
username = uname
password = pwd

imapobj = imapclient.IMAPClient(imap_server, ssl=True)
imapobj.login(username, password)

smtpobj = smtplib.SMTP(smtp_server, 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.login(username, password)
pprint.pprint(imapobj.list_folders())

imaplib._MAXLINE = 100000000

imapobj.select_folder('Inbox', readonly=False)
UIDs = imapobj.search(['SINCE', '01-Aug-2010', 'BEFORE', '01-Dec-2019'])