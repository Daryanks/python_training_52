from model.user import User

def test_add_user(app):
    app.user.edit_first_user(User("Second", "Ivan"))