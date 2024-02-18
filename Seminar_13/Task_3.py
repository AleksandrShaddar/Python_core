# Cоздайте класс с базовым исключением и дочерние классы-исключения:
# - ошибка уровня,
# - ошибка доступа.

class UserError(Exception):
    pass

class LevelError(UserError):
    pass

class AccessError(UserError):
    pass