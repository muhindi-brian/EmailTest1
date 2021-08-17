imapobj.select_folder('Inbox', readonly=False)

UIDs = imapobj.search(['SUBJECT', 'Best Buy'])
imapobj.delete_messages(UIDs)
imapobj.expunge()

# for Gmail, use this instead
imapobj.add_gmail_labels(UIDs,'\Trash')