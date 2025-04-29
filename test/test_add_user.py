# -*- coding: utf-8 -*-
import pytest
from model.user import User
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_user(app):
    app.session.login("admin", "secret")
    app.user.add_new(User("First", "User", "Home", "N.Novgorod", "112", "u.first@mail.ru", "1", "2001", "May"))
    app.session.logout()

