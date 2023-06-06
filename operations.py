from auxiliary import *
import json


def no_notes() -> bool:
    with open('Notes.json', encoding='UTF-8') as fp:
        notes = json.load(fp)
    if not notes:
        print('\nЗаметок нет ...\n')
        return True
    return False


def print_note(note: dict):
    print(f"ID: {note['ID']}")
    print(f"НАЗВАНИЕ: {note['title']}")
    print(f"СОДЕРЖИМОЕ:")
    print(note['content'])
    print(f"ПОСЛЕДНЕЕ ИЗМЕНЕНИЕ: {note['last_modified']}")
    print('----------------------------------------------------------')


def print_all():
    if no_notes():
        return
    with open('Notes.json', encoding='UTF-8') as fp:
        notes = json.load(fp)
    id_in_order = sorted(notes.keys(), key=lambda x: datetime.strptime(notes[x]['last_modified'], '%d/%m/%Y %H:%M:%S'))
    print("\nВсе заметки:\n")
    for note_id in id_in_order:
        print_note(notes[note_id])


def print_in_date_range():
    if no_notes():
        return
    print("\nПоиск заметок из диапазона дат:")
    print("Введите левую границу диапазона:")
    left_boundary = get_date()
    print()
    print("Введите правую границу диапазона:")
    right_boundary = get_date()
    with open('Notes.json', encoding='UTF-8') as fp:
        notes = json.load(fp)
    id_list = [note_id for note_id in notes if
               left_boundary <= datetime.strptime(notes[note_id]['last_modified'],
                                                  '%d/%m/%Y %H:%M:%S') <= right_boundary]
    if not id_list:
        print("\nНет заметок из указанного диапазона...\n")
        return
    id_list_in_order = sorted(id_list, key=lambda x: datetime.strptime(notes[x]['last_modified'], '%d/%m/%Y %H:%M:%S'))
    print(f"Заметки из диапазона {datetime.strftime(left_boundary, '%d/%m/%Y')} "
          f"- {datetime.strftime(right_boundary, '%d/%m/%Y')}:")
    for note_id in id_list_in_order:
        print_note(notes[note_id])


def get_note_by_id() -> dict:
    note_id = input("\nВведите ID заметки:")
    with open('Notes.json', encoding='UTF-8') as fp:
        notes = json.load(fp)
    note = notes.get(note_id, dict())
    return note


def note_search():
    if no_notes():
        return
    search_string = input("\nВведите строку для поиска:")
    with open('Notes.json', encoding='UTF-8') as fp:
        notes = json.load(fp)
    id_list = [note_id for note_id in notes
               if (search_string in (notes[note_id]['title'] + notes[note_id]['content']))]
    if not id_list:
        print("\nЗаметок не найдено...\n")
        return

    for note_id in id_list:
        notes[note_id]['title'] = notes[note_id]['title'].replace(search_string, search_string.upper())
        notes[note_id]['content'] = notes[note_id]['content'].replace(search_string, search_string.upper())
    id_list_in_order = sorted(id_list, key=lambda x: datetime.strptime(notes[x]['last_modified'], '%d/%m/%Y %H:%M:%S'))
    print(f"\nРезультаты поиска по запросу '{search_string}':\n")
    for note_id in id_list_in_order:
        print_note(notes[note_id])


def create_new_note():
    with open('Notes.json', encoding='UTF-8') as fp:
        notes = json.load(fp)

    new_note = dict()
    print("\nСоздание новой заметки:\n")

    new_note['title'] = input("Введите НАЗВАНИЕ заметки: ")

    print("Введите СОДЕРЖИМОЕ заметки,")
    new_note_content = get_multiline_input()

    new_note['content'] = new_note_content

    new_note['ID'] = max([int(note_id) for note_id in notes]) + 1 if notes else 1

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
    print('\nЗаметка удалена\n')


def delete_all():
    if no_notes():
        return
    with open('Notes.json', encoding='UTF-8') as fp:
        notes = json.load(fp)
    notes.clear()
    with open('Notes.json', 'w', encoding='UTF-8') as fp:
        json.dump(notes, fp, indent=4)
    print("\nВсе заметки удалены\n")


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
