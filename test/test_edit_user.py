from model.user import User

def test_add_user(app):
    if app.user.count() == 0:
        app.user.add_new(User(firstname="test"))
    old_users = app.user.get_users_list()
    user = User("Second", "Ivan")
    user.id = old_users[0].id
    app.user.edit_first_user(user)
    assert len(old_users) == app.user.count()
    new_users = app.user.get_users_list()
    old_users[0] = user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)