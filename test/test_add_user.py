# -*- coding: utf-8 -*-
from model.user import User

def test_add_user(app):
    old_users = app.user.get_users_list()
    user = User(firstname="Darya", lastname="Kash", address= "N.Novgorod", email= "u.first@mail.ru")
    app.user.add_new(user)
    assert len(old_users) + 1 == app.user.count()
    new_users = app.user.get_users_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)