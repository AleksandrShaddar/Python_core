# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

from collections import defaultdict
import json

class Factorial:
    def __init__(self, size, name_file='Task_2.json'):
        self.storage = defaultdict(int)
        self.size = size
        self.name_file = name_file

    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.storage.items()))
        return f'объекты хранилища:\n{txt}'

    def __call__(self, k):
        f = 1
        for i in range(2, k + 1):
            f *= i
        if len(self.storage) == self.size:
            self.storage.pop(list(self.storage)[0])
        self.storage[k] = f
        return f     
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        with open(self.name_file, 'w') as f_json:
            json.dump(self.storage, f_json, indent=4)
        self.storage.clear()

        
if __name__ == '__main__':
    ek = Factorial(5)
    with ek as f:
        for i in range(11):
            f(i)
        print(f"{f}")
        