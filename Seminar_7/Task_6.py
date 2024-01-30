# ✔ Дорабатываем функции из предыдущих задач. 
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции. 
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции 
# (добавьте проверки). 
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from pathlib import Path
import os


def sort_files_by_ext(path=None):
    if not path:
        path = Path().cwd()
    path = Path(path)
    files = Path(path).iterdir()
    os.chdir(path)

    for file in files:
        print(file.is_file(), Path(file.suffix) not in Path().iterdir())
        if (file.is_file()
                and Path(file.suffix) not in Path().iterdir()):
            os.mkdir(file.suffix)

        if file.is_file() and file.suffix != ".py":
            file.replace(rf"{file.suffix}\{file.name}")

if __name__ == '__main__':
    sort_file_by_ext()