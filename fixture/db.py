import pymysql.cursors
from model.group import Group
from model.user import User
class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_users_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(User(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_user_info_from_db_by_id(self, id):
        cursor = self.connection.cursor()
        try:
            user = []
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3 from addressbook where id=%s", id)
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                user.append(User(id=str(id), firstname=firstname, lastname=lastname, address=address, homephone=home, mobilephone=mobile, workphone=work, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return user


    def destroy(self):
        self.connection.close()