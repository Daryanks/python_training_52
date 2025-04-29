from model.user import User

def test_add_user(app):
    app.session.login("admin", "secret")
    app.user.edit_first_user(User("Second", "Ivan", "Ig", "Moscow", "001", "u.second@mail.ru", "5", "2025", "June"))
    app.session.logout()