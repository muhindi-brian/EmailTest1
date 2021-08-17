import imaplib
import pprint

pprint.pprint(imapobj.list_folders())

imaplib._MAXLINE = 10000000

imapobj.select_folder('Inbox', readonly=True)
UIDs = imapobj.search(['SINCE', '01-Aug-2019', 'BEFORE', '01-Dec-2019'])

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

rom_addresses = []
subjects = []
dates = []
days = []
months = []
years = []
times = []
sent_received = []
unsub_links = []

for i in range(len(UIDs)):
    raw_message = imapobj.fetch(UIDs[i], ['BODY[]'])
    message = pyzmail.PyzMessage.factory(raw_message[UIDs[i]][b'BODY[]'])

    if message.get_address('from')[1] == username:
        sent_received.append('Sent')
    else:
        sent_received.append('Received')

    full_date = message.get_decoded_header('date')
    from_addresses.append(message.get_address('from'))
    subjects.append(message.get_subject(''))
    unsub_link = message.get_decoded_header('List-Unsubscribe')
    if len(str(unsub_link)) > 0 and 'mailto' in unsub_link:
        unsub_link = unsub_link.split(',')
        unsub_links.append([unsub_link[idx] for idx, s in enumerate(unsub_link) if 'mailto' in s][0])
    else:
        unsub_links.append('No unsubscribe link found')

    day = full_date.split()[0].strip(',')
    date = full_date.split()[1]
    month = full_date.split()[2]
    year = full_date.split()[3]
    time = full_date.split()[4]

    days.append(day)
    dates.append(date)
    months.append(month)
    years.append(year)
    times.append(time)