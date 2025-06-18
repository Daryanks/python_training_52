from fixture.orm import ORMFixture
from model.group import Group
from model.user import User
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_group_list(app):
    groups = db.get_group_list()
    if len (db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(groups)
    users = db.get_users_not_in_group(group)
    if db.get_users_not_in_group(group) == 0:
        app.user.add_new(User(firstname="test"))
    users_in_group = db.get_users_in_group(group)
    user = random.choice(users)
    user_id = user.id
    app.user.add_user_to_group(user_id, group)
    new_users_in_group = db.get_users_in_group(group)
    users_in_group.append(user)
    assert sorted(users_in_group, key=User.id_or_max) == sorted(new_users_in_group, key=User.id_or_max)

