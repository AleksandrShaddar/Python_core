# Напишите программу банкомат. 
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег


account = 0
counter = 0
maximum = 0

while True: 
    print(f"Ваш баланс: {account}")
    action = int(input("Выберете действие: 1 - пополнить, 2 - снять, 3 - выйти: "))
    match action:
        case 1:
            act_1 = int(input("Введите сумму пополнения кратную 50: "))
            if maximum >= 5000000:
                print(f"Превышен лимит операций. Налог на богатство {account*0.1}")
                account -= account*0.1
            if act_1 % 50 == 0:
                maximum += act_1
                account += act_1
                counter +=1
                if counter == 3:
                    account += account*0.03
                    print(f"За 3 операции наичслено {account*0.03}")
                    counter = 0
            else:
                if maximum >= 5000000:
                    print(f"Превышен лимит операций. Налог на богатство {account*0.1}")
                    account -= account*0.1
                continue
        case 2:
            act_2 = int(input("Введите сумму снятия кратную 50: "))
            if maximum >= 5000000:
                print(f"Превышен лимит операций. Налог на богатство {account*0.1}")
                account -= account*0.1
            if act_2 % 50 == 0 and account >= act_2:  
                procent = min([max([act_2*0.015, 30]), 600])              
                account -= act_2 + procent
                print(f"Комиссия за операцию: {procent}")
                counter +=1                
                if counter == 3:
                    account += account*0.03
                    print(f"За 3 операции наичслено: {account*0.03}")
                    counter = 0
            else:
                if maximum >= 5000000:
                    print(f"Превышен лимит операций. Налог на богатство {account*0.1}")
                    account -= account*0.1
                continue
        case 3:
            quit()