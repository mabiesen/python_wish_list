import smtplib
import imaplib


# also need a method to obtain email header information!!!!

class GmailClass:

  gmailuser = ""
  gmailpassword = ""

  def __init__(self, user, password):
    self.gmailuser = user
    self.gmailpassword = password

  def send_email(self, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
      server = smtplib.SMTP("smtp.gmail.com", 587)
      server.ehlo()
      server.starttls()
      server.login(self.gmailuser, self.gmailpassword)
      server.sendmail(FROM, TO, message)
      server.close()
      print 'successfully sent the mail'
    except:
      print "failed to send mail"



  def read_email_from_gmail(self):
    try:
      mail = imaplib.IMAP4_SSL(SMTP_SERVER)
      mail.login(self.gmailuser,self.gmailpassword)
      mail.select('inbox')

      type, data = mail.search(None, 'ALL')
      mail_ids = data[0]

      id_list = mail_ids.split()
      first_email_id = int(id_list[0])
      latest_email_id = int(id_list[-1])


      for i in range(latest_email_id,first_email_id, -1):
        typ, data = mail.fetch(i, '(RFC822)' )

          for response_part in data:
            if isinstance(response_part, tuple):
              msg = email.message_from_string(response_part[1])
              email_subject = msg['subject']
              email_from = msg['from']
              print 'From : ' + email_from + '\n'
              print 'Subject : ' + email_subject + '\n'

    except Exception, e:
      print str(e)
