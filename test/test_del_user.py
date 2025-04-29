def test_delete_first_user(app):
    app.session.login("admin", "secret")
    app.user.delete_first_user()
    app.session.logout()