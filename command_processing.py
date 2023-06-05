from operations import *
from menu import *


def main_menu_command_handler(command: str):
    match command:
        case '1':
            print_all()
        case '2':
            print_in_date_range()
        case '3':
            note_search()
        case '4':
            note = get_note_by_id()
            if note:
                print("\nРАБОТА С ЗАМЕТКОЙ:")
                print_note(note)
                note_processing_menu_command_handler(note_managing_menu_command(), note)
            else:
                print("Нет заметки с таким ID")
        case '5':
            create_new_note()
        case '6':
            delete_all()
        case _:
            pass


def note_processing_menu_command_handler(command: str, note: dict):
    match command:
        case '1':
            delete_note(note)
        case '2':
            edit_note(note)
        case _:
            pass