from Student import Student
import pytest


@pytest.fixture
def st_1():
    return Student("Иван Иванов", "subjects.csv")


def test_subject(st_1):
    with pytest.raises(ValueError):
        st_1.add_grade("Биология", 4)


def test_name():
    with pytest.raises(ValueError):
        Student("Иван 228", "subjects.csv")


def test_add_grade(st_1):
    with pytest.raises(ValueError):
        st_1.add_grade("Математика", 6)


def test_test_score(st_1):
    with pytest.raises(ValueError):
        st_1.add_test_score("История", 105)


def test_average_test_score(st_1):
    st_1.add_test_score("Физика", 60)
    st_1.add_test_score("Физика", 80)
    assert st_1.get_average_test_score("Физика") == 70.0


def test_average_grade(st_1):
    st_1.add_grade("Математика", 4)
    st_1.add_grade("История", 5)
    assert st_1.get_average_grade() == 4.5
