# Функция принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# Вернуть словарь с именем в качестве ключа и суммой премии 
# в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии


def get_dict(lst1: list, lst2: list, lst3: list) -> dict[str, float]:
    """
    """
    res = {}
    for name, salary, bonus in zip(lst1, lst2, lst3):
        res[name] = salary * float(bonus.replace('%', '')) / 100
    return res

a = ["Python", "Rust", "Java"]
b = [100, 137, 89]
c = ["10.4%", "10.0%", "12.5%"]

print(get_dict(a, b, c))