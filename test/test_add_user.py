# -*- coding: utf-8 -*-
from model.user import User

def test_add_user(app):
    old_users = app.user.get_users_list()
    user = User(firstname="User", lastname="First", address= "N.Novgorod", email= "u.first@mail.ru", homephone="12548", workphone="+4587", mobilephone="254(876)", faxphone="128")
    app.user.add_new(user)
    assert len(old_users) + 1 == app.user.count()
    new_users = app.user.get_users_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)