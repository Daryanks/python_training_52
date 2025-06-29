from model.user import User
import re

def test_user_info_compare(app):
    user_from_home_page = app.user.get_users_list()[0]
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_home_page.id == user_from_edit_page.id
    assert user_from_home_page.firstname == clear(user_from_edit_page.firstname)
    assert user_from_home_page.lastname == clear(user_from_edit_page.lastname)
    assert user_from_home_page.address == clear(user_from_edit_page.address)
    assert user_from_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(user_from_edit_page)
    assert user_from_home_page.all_emails_from_homepage == merge_emails_like_on_home_page(user_from_edit_page)

def clear(s):
   return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(user):
   return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [user.homephone, user.mobilephone, user.workphone]))))

def merge_emails_like_on_home_page(user):
   return "\n".join(filter(lambda x: x is not None and x != "", [user.email, user.email2, user.email3]))