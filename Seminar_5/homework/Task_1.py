# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

file_path = "C:/Users/User/Documents/example.txt"


def get_file_info(file_path):
    *adress, name_type = file_path.split('/') 
    *name, type_doc = name_type.split('.')
    type_doc = '.' + type_doc
    adress_doc = ''
    for i in adress:
        adress_doc += i + '/'
    name_doc = ''
    for i in name:
        if i != name[len(name) - 1]:
            name_doc += i + '.'
        else:
            name_doc += i            
    return adress_doc, name_doc, type_doc

# или

def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)