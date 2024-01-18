# Три друга взяли вещи в поход. Сформируйте словарь, 
# где ключ — имя друга, а значение — кортеж вещей. 
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. 
# Код должен расширяться на любое большее количество друзей.

friends = {
    'Афанасий' : ('баян', 'бинокль', 'велосипед', 'спички'),
    'Борис' : ('баян', 'бинокль', 'велосипед', 'кружка'),
    'Владимир' : ('розетка', 'бритва', 'велосипед', 'кружка'),
    }

all_things = []

for things in friends.values():
    all_things.extend(things)

all_things_unique = set(all_things)

for key, value in friends.items():
    set_2 = set()    
    for item in value:
        if all_things.count(item) == 1:
            set_2.add(item)
    print(f"{set_2} только у {key}" if len(set_2) > 0 else f"У {key} нет уникальных вещей")
    set_2.clear()

for key, value in friends.items():
    set_1 = set() 
    for item in all_things:
        if item not in value and all_things.count(item) == len(friends) - 1:            
            set_1.add(item)
    print(f"{key} не взял {set_1}" if len(set_1) > 0 else f"{key} взял все вещи")
    set_1.clear()

print("Друзья взяли следующие вещи: ", all_things_unique)
