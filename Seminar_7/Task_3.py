# ✔ Напишите функцию, которая открывает на чтение созданные 
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните 
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя 
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя 
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, 
# сколько в более длинном файле. 
# ✔ При достижении конца более короткого файла, 
# возвращайтесь в его начало.


def get_file_number_of_lines(file) -> int:
    with open(file, 'r') as f:
        return len(f.readlines())
        # return sum(1 for i in f if i)


def read_or_begin(file) -> str:
    current = file.readline().rstrip()
    if not current:
        file.seek(0)
        current = file.readline().rstrip()
    return current


def combine_two_files(file1, file2, output):
    len_f1 = get_file_number_of_lines(file1)
    len_f2 = get_file_number_of_lines(file2)

    with (
        open(file1, 'r') as f1,
        open(file2, 'r') as f2,
        open(output, 'w') as out,
    ):
        # print(type(f1), type(f2), type(out))  # <class '_io.TextIOWrapper'>
        for _ in range(max(len_f1, len_f2)):
            name = read_or_begin(f1)
            numbers = read_or_begin(f2)

            a, b = numbers.replace(' ', '').split('|')
            mul = float(a) * float(b)

            if mul < 0:
                out.write(f'{name.lower()} {abs(mul)}\n')
            else:
                out.write(f'{name.upper()} {round(mul)}\n')


if __name__ == '__main__':
    # print(get_file_number_of_lines('numbers.txt'))
    # print(get_file_number_of_lines('names.txt'))
    combine_two_files('names.txt', 'numbers.txt', 'output.txt')