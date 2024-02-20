# Доработайте классы исключения так, чтобы они выдали
# подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.

class ProjectException(Exception):
    pass

class LevelError(ProjectException):
    def __init__(self, level_user, level_admin):
        self.level_user = level_user
        self.level_admin = level_admin

    def __str__(self):
        return f'Уровень пользователя ({self.level_user}) меньше чем ваш уровень ({self.level_admin})'


class AccessError(ProjectException):
    def __init__(self, user):
        self.user = user

    def __str__(self):
        return f'Пользователя {self.user} не существует'
