# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def get_dict(text: str) -> dict[str, int]:
    """
    """
    unicode_dict = {}
    num_1, num_2 = map(int, text.split())
    for i in range(min(num_1, num_2), max(num_1, num_2)):
        unicode_dict[chr(i)] = i
    return unicode_dict

print(get_dict('26 34'))