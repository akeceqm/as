import os
from eur import check_current_euro
from usd import check_current_dollar

def clear_console():
    os.system('cls')

print("Здравствуйте!")

balance_rub = 0
balance_usd = 0
balance_eur = 0
target_list = {}

def replenish_the_budget(replenish_the_budget_input):
    global balance_rub
    while True:
        if replenish_the_budget_input=="" or " " in replenish_the_budget_input :
            print("Неккоректный ввод")
            replenish_the_budget_input=str(input("Введите сумму для взноса: "))
        else:
            replenish_the_budget_input = float(replenish_the_budget_input)
            if replenish_the_budget_input > 0:
                balance_rub += replenish_the_budget_input
                break
            else:
                print("Введите сумму больше нуля.")
                replenish_the_budget_input=float(input("Введите сумму для взноса: "))

def make_expenses(make_expenses_input):
    global balance_rub
    while True:
        if make_expenses_input=="" or " " in make_expenses_input :
            print("Неккоректный ввод")
            make_expenses_input=str(input("Внести расходы: "))
        else:
            if "-" in make_expenses_input or "+" in make_expenses_input or "=" in make_expenses_input or "/" in make_expenses_input:
                print("Вы вели неккоректный ввод")
                make_expenses_input=str(input("Внести расходы: "))
            else:
                make_expenses_input = float(make_expenses_input)
                if make_expenses_input>balance_rub:
                    print("Ваш баланс меньше, чем ваш вычет из него")
                    make_expenses_input=str(input("Внести расходы: "))
                else:
                    balance_rub-=make_expenses_input
                    break

def check_wallet():
    global balance_rub
    global balance_usd
    global balance_eur
    usd_rate = check_current_dollar()
    eur_rate = check_current_euro()
    balance_usd = round(balance_rub/usd_rate,2)
    balance_eur = round(balance_rub/eur_rate,2)
    print(f"Баланс в рублях: {balance_rub}")
    print(f"Баланс в долларах: {balance_usd}")
    print(f"Баланс в евро: {balance_eur}")

def target_wallet():
    global target_list
    global balance_rub
    global balance_usd
    global balance_eur
    global target_input_money
    while True:
        if not target_list:
            print("У вас нет цели!")
        else:
            print("Ваши цели:")
            for target in target_list:
                print(f'{target}:{target_input_money}|Рубелй:{balance_rub}|Долларов:{balance_usd}|Евро:{balance_eur}|')
        target_input_variant = input("Хотите добавить цель? (y/n): ")
        if target_input_variant.lower() == "y":
            target_input = input("Ваша цель: ")
            target_input_money = (input("Введите сумму которая нужна для цели: "))
            while True:
                try:
                    target_input_money = float(target_input_money)
                    if target_input_money <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Введите корректную положительную сумму: ")
                    target_input_money = input("Введите сумму которая нужна для цели: ")

            target_list[target_input] = target_input_money

        elif target_input_variant.lower() == "n":
            return
            
def wallet():
    print('Пополнить буджет-1\nВнести расходы-2\nПосмотреть баланс-3\nПросмотреть цели-4')
    variant_input = (input("Ваш ответ: "))
    while True:
        if variant_input =="1":
            replenish_the_budget(replenish_the_budget_input=str(input("Введите сумму для взноса: ")))
            clear_console()
            wallet()
        elif variant_input =="2":
            make_expenses(make_expenses_input=str(input("Внести расходы: ")))
            if balance_rub<=0:
                print("Ваш баланс равнятеся 0 или меньше 0\nПоэтому этa операция не сработала!")
            clear_console()
            wallet()
            break
        elif variant_input =="3":
            clear_console()
            check_wallet()
            wallet()
            break
        elif variant_input =="4":
            clear_console()
            target_wallet()
            clear_console()
            wallet()
            break
            

        else:
            variant_input = (input("Ваш ответ: "))

def variant_language(language):
    while True:
        if language == 'ru':
            print("Выбран русский язык")
            wallet()
            break
        elif language == 'en':
            print("Выбран английский язык")
            break
        else:
            language = input("Введите корректный ответ: ")


variant_language(language=input('Введите язык ru или en: '))