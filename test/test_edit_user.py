from model.user import User
import random

def test_add_user(app, db, check_ui):
    if db.get_user_list() == 0:
        app.user.add_new(User(firstname="test"))
    old_users = db.get_user_list()
    user = random.choice(old_users)
    user_id = user.id
    modify_user = User(firstname="New_Second", lastname="Ivan")
    app.user.edit_user_by_id(modify_user, user_id)
    new_users = db.get_user_list()
    index = 0
    for contact in old_users:
        if user_id == contact.id:
            break
        index += 1
    old_users[index] = modify_user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
    if check_ui:
        assert sorted(new_users, key=User.id_or_max) == sorted(app.user.get_users_list(), key=User.id_or_max)