# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json


def txt_to_json(file_sourse: str, file_output: str):
    data_dict = {}

    with open (file_sourse, 'r', encoding='utf-8') as f:
        data = f.read()

    for line in data.split('\n'):
        name, number = line.split(' ')
        data_dict[name.capitalize()] = float(number)    

    with open (file_output, 'w') as f:
        json.dump(data_dict, f, indent=4)

txt_to_json('task1.txt', 'task1.json')

