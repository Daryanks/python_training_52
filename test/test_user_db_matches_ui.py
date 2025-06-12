import re

def test_user_info_compare(app, db):
    index = 0
    for user in app.user.get_users_list():
        index += 1
        user_from_home_page = app.user.get_users_list()[index]
        user_id = user_from_home_page.id
        user_from_db = db.get_user_info_from_db_by_id(user_id)
        assert user_from_home_page.firstname == clear(user_from_db[0].firstname)
        assert user_from_home_page.lastname == clear(user_from_db[0].lastname)
        assert user_from_home_page.address == clear(user_from_db[0].address)
        assert user_from_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(user_from_db[0])
        assert user_from_home_page.all_emails_from_homepage == merge_emails_like_on_home_page(user_from_db[0])


def clear(s):
   return re.sub("[() " " -]", "", s)

def merge_phones_like_on_home_page(user):
   return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [user.homephone, user.mobilephone, user.workphone]))))

def merge_emails_like_on_home_page(user):
   return "\n".join(filter(lambda x: x is not None and x != "", [user.email, user.email2, user.email3]))

