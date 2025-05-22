# -*- coding: utf-8 -*-
from model.user import User
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone(prefix, maxlen):
    symbols = string.digits + " "*3
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + prefix

testdata = [User(firstname=random_string("User", 7), lastname=random_string("lastname", 7), address=random_string("", 10), email=random_email("@mail.ru", 10), homephone=random_phone("+7", 10))
    for i in range(5)
]

@pytest.mark.parametrize("user", testdata, ids=(repr(x) for x in testdata))
def test_add_user(app, user):
    old_users = app.user.get_users_list()
    app.user.add_new(user)
    assert len(old_users) + 1 == app.user.count()
    new_users = app.user.get_users_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)