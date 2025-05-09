from model.user import User

def test_add_user(app):
    if app.user.count() == 0:
        app.user.add_new(User(firstname="test"))
    app.user.edit_first_user(User("Second", "Ivan"))