from model.user import User
import random
def test_delete_some_user(app, db, check_ui):
    if app.user.count() == 0:
        app.user.add_new(User(firstname="test"))
    old_users = db.get_user_list()
    user = random.choice(old_users)
    app.user.delete_user_by_id(user.id)
    new_users = db.get_user_list()
    old_users.remove(user)
    assert old_users == new_users
    if check_ui:
        assert sorted(new_users, key=User.id_or_max) == sorted(app.user.get_users_list(), key=User.id_or_max)