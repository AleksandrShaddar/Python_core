# Напишите функцию, которая принимает строку текста. 
# Сформируйте список с уникальными кодами Unicode 
# каждого символа введённой строки отсортированный по убыванию.


def uniq_symbols(text: str) -> list[int]:
    """
    """
    list_unicode = set()
    for char in text:
        list_unicode.add(ord(char))
    return sorted(list_unicode, reverse=True)


text = "каждого символа введённой строки отсортированный по убыванию"

print(uniq_symbols(text))