from fixture.orm import ORMFixture
from model.group import Group
from model.user import User
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_delete_user_from_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = db.get_group_list()
    group = random.choice(groups)
    if len(db.get_users_in_group(group)) == 0:
        users_not_in_group = db.get_users_not_in_group(group)
        user = random.choice(users_not_in_group)
        user_id = user.id
        app.user.add_user_to_group(user_id, group)
    users_in_group = db.get_users_in_group(group)
    user_g = random.choice(users_in_group)
    user_id = user_g.id
    app.user.delete_user_from_group(user_id, group)
    new_users_in_group = db.get_users_in_group(group)
    users_in_group.remove(user_g)
    assert sorted(users_in_group, key=User.id_or_max) == sorted(new_users_in_group, key=User.id_or_max)