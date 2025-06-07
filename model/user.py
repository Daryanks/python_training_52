from sys import maxsize
class User:
    def __init__(self, id=None, firstname=None, lastname=None, company=None, address=None, home=None, email=None, all_phones_from_homepage=None, homephone=None, workphone=None, mobilephone=None, faxphone=None, all_emails_from_homepage=None, email2=None, email3=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.home = home
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.faxphone = faxphone
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize