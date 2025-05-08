# -*- coding: utf-8 -*-
from model.user import User

def test_add_user(app):
    app.user.add_new(User("First", "User", "Home", "N.Novgorod", "112", "u.first@mail.ru"))