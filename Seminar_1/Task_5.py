# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

FORMAT = 15


def print_mult(n, m):
    for i in range(2, 11):
        st = ''
        for j in range(n, m + 1):
            mult = j * i
            st0 = f'{j} X {i} = {mult}'
            st += st0 + ' ' * (FORMAT - len(st0))
        print(st)


print_mult(2, 5)

print()

print_mult(6, 9)


# или

for i in [2, 6]:
    for j in range(2, 11):
        for k in range(i, i+4):
            print(f"{k:>1} X {j:>2} = {k*j:>2}", end="\t")
        print()
    print()
