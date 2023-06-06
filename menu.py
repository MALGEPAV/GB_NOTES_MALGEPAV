from auxiliary import *


def main_menu_command() -> str:
    print("ГЛАВНОЕ МЕНЮ")
    print("""Введите номер команды:
    "1": Вывод ВСЕХ заметок на экран
    "2": Вывод заметок из диапазона дат
    "3": Поиск заметки по названию и содержимому
    "4": Работа с заметкой по ID
    "5": Создать новую заметку
    "6": Удалить ВСЕ заметки
    "0": Завершение работы
    """)
    command = get_correct_input(lambda x: x.strip() in ['1', '2', '3', '4', '5', '6', '0'])
    return command


def note_managing_menu_command() -> str:
    print("""Введите номер команды:
        "1": Удалить выбранную заметку
        "2": Редактировать выбранную заметку
        "0": Главное меню
        """)
    command = get_correct_input(lambda x: x.strip() in ['1', '2', '0'])
    return command
