from Task_7 import Project, User, load_users, LevelError, AccessError, ProjectException

import json
import os

import pytest

@pytest.fixture
def authed_project(request):
    file = 'test_users.json'
    data = {"5": {"12345656": "Alex"}, "7": {"12345657": "Ben"}}
    with open(file, 'w') as f:
        json.dump(data, f)
    p = Project(file)
    p.auth("12345656", "Alex")

    def delete_project():
        os.remove(file)

    request.addfinalizer(delete_project)

    return p


@pytest.fixture
def authed_user():
    return User('12345656', '5', 'Alex')


def test_user_authed(authed_project, authed_user):
    assert authed_project.admin is not None
    assert authed_project.admin == authed_user


if __name__ == '__main__':
    pytest.main(['-vv'])