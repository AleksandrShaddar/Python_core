# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.

def game(text: str, answers: list[str], numb_try: int) -> int:
    print(text)
    for i in range(1, numb_try + 1):
        answer = input("Введите ответ: ")
        if answer in answers:
            return i
    return 0


text = "Какое животное называют 'косолапый' ?"
answers = ['медведь', 'мишка']

print(game(text, answers, 2))