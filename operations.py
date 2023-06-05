from datetime import datetime
import json


def print_all():
    with open('Notes.json', encoding='UTF-8') as fp:
        notes = json.load(fp)
    if not notes:
        print('Заметок нет...')
        return
    for note in notes.values():
        print_note(note)


def print_in_date_range():
    pass


def get_note_by_id() -> dict:
    note_id = input("Введите ID заметки:")
    with open('Notes.json', encoding='UTF-8') as fp:
        notes = json.load(fp)
    note = notes.get(note_id, dict())
    return note


def note_search():
    pass


def create_new_note():
    with open('Notes.json', encoding='UTF-8') as fp:
        notes = json.load(fp)

    new_note = dict()

    new_note['title'] = input("Введите НАЗВАНИЕ заметки: ")

    print("Введите СОДЕРЖИМОЕ заметки:\n Для завершения ввода введите пустую строку:")
    new_note_content = ''
    new_line = input()
    while new_line != '':
        new_note_content += new_line + '\n'
        new_line = input()
    new_note['content'] = new_note_content

    new_note['ID'] = max([int(note_id) for note_id in notes.keys()]) + 1 if notes else 1

    new_note['last_modified'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    notes[new_note['ID']] = new_note

    print("Заметка")
    print_note(new_note)
    print("добавлена")

    with open('Notes.json', 'w', encoding='UTF-8') as fp:
        json.dump(notes, fp, indent=4)


def delete_note(note: dict):
    with open('Notes.json', encoding='UTF-8') as fp:
        notes = json.load(fp)
    notes.pop(str(note['ID']))
    with open('Notes.json', 'w', encoding='UTF-8') as fp:
        json.dump(notes, fp, indent=4)


def delete_all():
    with open('Notes.json', encoding='UTF-8') as fp:
        notes = json.load(fp)
    notes.clear()
    with open('Notes.json', 'w', encoding='UTF-8') as fp:
        json.dump(notes, fp, indent=4)
    print("Все заметки удалены")


def edit_note(note: dict):
    print("Редактирование заметки:")
    print("""Редактировать название?:
            "1": Да
            "2": Нет
            """)
    command = input('Ввод: ').strip()
    while command not in ('1', '2'):
        print('Некорректный ввод, попробуйте еще раз:')
        command = input('Ввод: ').strip()
    match command:
        case '1':
            note['title'] = input("Введите новое название: ")
        case '2':
            pass

    print("""Редактировать содержимое?:
                "1": Да
                "2": Нет
                """)
    command = input('Ввод: ').strip()
    while command not in ('1', '2'):
        print('Некорректный ввод, попробуйте еще раз:')
        command = input('Ввод: ').strip()
    match command:
        case '1':
            print("Введите новое содержимое заметки:\n Для завершения ввода введите пустую строку:")
            new_note_content = ''
            new_line = input()
            while new_line != '':
                new_note_content += new_line + '\n'
                new_line = input()
            note['content'] = new_note_content
        case '2':
            pass
    note['last_modified'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print("Заметка успешно отредактирована:")
    print_note(note)
    with open('Notes.json', encoding='UTF-8') as fp:
        notes = json.load(fp)
    notes[note['ID']] = note
    with open('Notes.json', 'w', encoding='UTF-8') as fp:
        json.dump(notes, fp, indent=4)


def print_note(note: dict):
    print(f"ID: {note['ID']}")
    print(f"НАЗВАНИЕ: {note['title']}")
    print(f"СОДЕРЖИМОЕ:")
    print(note['content'])
    print(f"ПОСЛЕДНЕЕ ИЗМЕНЕНИЕ: {note['last_modified']}")
    print('----------------------------------------------------------')