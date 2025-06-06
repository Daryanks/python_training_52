from model.group import Group
import random

def test_edit_group(app, db, check_ui):
    if db.get_group_list() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    gr_id = group.id
    modify_group = Group(name="New_group")
    app.group.edit_group_by_id(gr_id, modify_group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    index = 0
    for gr in old_groups:
        if gr_id == gr.id:
            break
        index += 1
    old_groups[index] = modify_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)