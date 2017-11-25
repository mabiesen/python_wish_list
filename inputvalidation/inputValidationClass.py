import re
import datetime
import urlparse


class validateInput:

    def __init__(self):
        print("Input validation initiated")

    def validate_url(self,myurl):
        analysis = urlparse.urlparse(myurl)
        print(analysis)
        if analysis[0] != '' and analysis[1] != '':
            return True
        return False

    def validate_email(self,emailaddr):
        if re.match(r"[^@]+@[^@]+\.[^@]+", emailaddr):
            return True
        return False

    def validate_number_between(self, start, finish, myinput):
        if myinput <= finish and myinput >= start:
            return True
        return False

    def validate_is_date(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%m-%d-%Y')
            return True
        except ValueError:
            return False
