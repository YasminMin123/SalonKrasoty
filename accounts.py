import functions as func

def return_to_pos_menu():
    return input("Нажмите Enter для продолжения..."), posetitel()

def posetitel():
    pos_Choice = int(input("""
Приветствую дорогой, Посетитель!
Пожалуйста наберите номер меню для работы с программой, если закончили, то наберите 6:

	1)	Показать историю посещений 
	2)	Показать последнюю дату посещения
	3)	Показать историю оплаты 
	4)	Показать расписание к тренировкам 
	5)	Показать мою информацию
	6)	Выход

    Выбор: => """))
    if pos_Choice == 1:
        print('\n',func.show_history_of_visiting(),'\n')
        return_to_pos_menu()
    elif pos_Choice == 2:
        print('\nПоследняя дата посещения: ',func.show_last_date())
        return_to_pos_menu()
    elif pos_Choice == 3:
        print(func.show_history_of_paying(input('Как зовут посетителя? ')))
        return_to_pos_menu()
    elif pos_Choice == 4:
        func.show_raspisanie()
        return_to_pos_menu()
    elif pos_Choice == 5:
        print(func.show_about_me())
        return_to_pos_menu()


def return_to_per_menu():
    return input("Нажмите Enter для продолжения..."), personal()

def personal():
    per_Choice = int(input(
"""Приветствую уважаемый Персонал!
Пожалуйста наберите номер меню для работы с программой, если закончили, то наберите 7:

	•	Показать список процедур
	•	Найти посетителя
	•	Показать все процедуры
	•	Показать расписание к процедурам
	•	Купить процедуру
	•	Найти процедуры
	•	Выход (Выходит из программы)

Выбор меню >> """))
    if per_Choice == 1:
        func.get_proc()
        return_to_per_menu()
    elif per_Choice == 2:
        func.find_visiter()
        return_to_per_menu()
    elif per_Choice == 3:
        print(func.show_proc())
        return_to_per_menu()
    elif per_Choice == 4:
        print(func.time_proc())
        return_to_per_menu()
    elif per_Choice == 5:
        func.buy_proc()
        return_to_per_menu()
    elif per_Choice == 6:
        print(func.find_proc())
        return_to_per_menu()
    elif per_Choice == 7:
        exit(print('Спасибо за использование системы!'))


def return_to_man_menu():
    return input("Нажмите Enter для продолжения..."), manager()


def manager():
    man_Choice = int(input('''
    1. Показать список посетителей 
    2. Показать количество посетителей 
    3. Поиск посетителя
    4. Изменить цену для процедур
    5. Изменить время - название процедур
    6. Показать посетителя с максимальным количеством посещений
    7. Показать посетителя с минимальным количеством посещений
    8. Выход (Выходит из программы)

Выбор --> '''
    ))

    if man_Choice == 1:
        print(func.show_list_of_visiters())
        return_to_man_menu()
    elif man_Choice == 2:
        print(func.number_of_visitors())
        return_to_man_menu()
    elif man_Choice == 3:
        print(func.find_client())
        return_to_man_menu()



if __name__ == '__main__':
    manager()