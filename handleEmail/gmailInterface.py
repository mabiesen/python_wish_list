import smtplib
import imaplib


class GmailHelper:

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
          
          
         
  def retrieve_email(self):
    
