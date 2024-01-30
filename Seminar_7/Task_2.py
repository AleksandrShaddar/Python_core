# ✔ Напишите функцию, которая генерирует 
# псевдоимена. 
# ✔ Имя должно начинаться с заглавной буквы, 
# состоять из 4-7 букв, среди которых 
# обязательно должны быть гласные. 
# ✔ Полученные имена сохраните в файл.

from string import ascii_lowercase
from random import choice, randint

VOWELS = 'a', 'o', 'e', 'i', 'u', 'y'
LETTERS = ascii_lowercase


def generate_pseudonyms(min_len=3, max_len=6) -> str:
    name = choice(VOWELS).upper() + ''.join(choice(LETTERS) for _ in range(randint(min_len, max_len)))
    return name


def save_name_to_file(file_name: str, rows: int):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines('\n'.join(generate_pseudonyms() for _ in range(rows)))


if __name__ == '__main__':
    save_name_to_file('names.txt', 5)