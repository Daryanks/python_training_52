from model.user import User


def test_users_list(app, db):
    user_list = app.user.get_users_list()
    def clean(user):
        return User(id=user.id, firstname=user.firstname.strip(), lastname=user.lastname.strip())
    db_list = map(clean, db.get_users_list())
    assert sorted(user_list, key=User.id_or_max) == sorted(db_list, key=User.id_or_max)