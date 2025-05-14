from model.user import User
from random import randrange

def test_add_user(app):
    if app.user.count() == 0:
        app.user.add_new(User(firstname="test"))
    old_users = app.user.get_users_list()
    index = randrange(len(old_users))
    user = User("Second", "Ivan")
    user.id = old_users[index].id
    app.user.edit_user_by_index(user, index)
    assert len(old_users) == app.user.count()
    new_users = app.user.get_users_list()
    old_users[index] = user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)