from model.group import Group

def test_edit_first_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group("Test17", "test17", "test17"))
    app.session.logout()