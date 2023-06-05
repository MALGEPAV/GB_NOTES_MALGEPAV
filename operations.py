from auxiliary import *
import json


def print_note(note: dict):
    print(f"ID: {note['ID']}")
    print(f"НАЗВАНИЕ: {note['title']}")
    print(f"СОДЕРЖИМОЕ:")
    print(note['content'])
    print(f"ПОСЛЕДНЕЕ ИЗМЕНЕНИЕ: {note['last_modified']}")
    print('----------------------------------------------------------')


def print_all():
    with open('Notes.json', encoding='UTF-8') as fp:
        notes = json.load(fp)
    if not notes:
        print('Заметок нет...')
        return
    id_in_order = sorted(notes.keys(), key=lambda x: datetime.strptime(notes[x]['last_modified'], '%d/%m/%Y %H:%M:%S'))
    for note_id in id_in_order:
        print_note(notes[note_id])


def print_in_date_range():
    print("Введите левую границу диапазона:")
    left_boundary = get_date()
    print()
    print("Введите правую границу диапазона:")
    right_boundary = get_date()
    with open('Notes.json', encoding='UTF-8') as fp:
        notes = json.load(fp)
    id_list = [note_id for note_id in notes.keys() if
               left_boundary <= datetime.strptime(notes[note_id]['last_modified'],
                                                  '%d/%m/%Y %H:%M:%S') <= right_boundary]
    id_list_in_order = sorted(id_list, key=lambda x: datetime.strptime(notes[x]['last_modified'], '%d/%m/%Y %H:%M:%S'))
    print(f"Заметки из диапазона {datetime.strftime(left_boundary, '%d/%m/%Y')} "
          f"- {datetime.strftime(right_boundary, '%d/%m/%Y')}:")
    for note_id in id_list_in_order:
        print_note(notes[note_id])


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

    print("Введите СОДЕРЖИМОЕ заметки,")
    new_note_content = get_multiline_input()

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
    command = get_correct_input(lambda x: x.strip() in ['1', '2'])

    match command:
        case '1':
            note['title'] = input("Введите новое название: ")
        case '2':
            pass

    print("""Редактировать содержимое?:
                "1": Да
                "2": Нет
                """)
    command = get_correct_input(lambda x: x.strip() in ['1', '2'])

    match command:
        case '1':
            print("Введите новое содержимое заметки,")
            new_note_content = get_multiline_input()
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
