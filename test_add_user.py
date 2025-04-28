# -*- coding: utf-8 -*-
import pytest
from user import User
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_user(app):
    app.login("admin", "secret")
    app.add_new_user(User("First", "User", "Home", "N.Novgorod", "112", "u.first@mail.ru", "1", "2001", "May"))
    app.logout()

