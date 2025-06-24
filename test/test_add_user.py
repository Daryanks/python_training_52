# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app, db, json_users, check_ui):
    user = json_users
    old_users = db.get_users_list()
    app.user.add_new(user)
    assert len(old_users) + 1 == app.user.count()
    new_users = db.get_users_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
    if check_ui:
        assert sorted(new_users, key=User.id_or_max) == sorted(app.user.get_users_list(), key=User.id_or_max)
