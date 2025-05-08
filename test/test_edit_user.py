from model.user import User

def test_add_user(app):
    app.session.login("admin", "secret")
    app.user.edit_first_user(User("Second", "Ivan"))
    app.session.logout()