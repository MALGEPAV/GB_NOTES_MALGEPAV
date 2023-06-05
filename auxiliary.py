from datetime import datetime


def get_correct_input(condition) -> str:
    input_str = input("Ввод: ")
    while not condition(input_str):
        print("Некорректный ввод, попробуйте еще раз.")
        input_str = input("Ввод: ")
    return input_str


def is_leap(year: int) -> bool:
    return (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)


def day_is_correct(day: str, month: str, year: str) -> bool:
    day = int(day)
    month = int(month)
    year = int(year)
    if month != 2:
        return 1 <= day <= 30 + (month + int((month - 0.5) / 7)) % 2
    return 1 <= day <= 28 + int(is_leap(year))


def get_date() -> datetime:
    print("Введите год (не меньше 2000 и не больше текущего):")
    year = get_correct_input(lambda x: x.isdigit() and (1900 <= int(x) <= int(str(datetime.now())[:4])))
    print("Введите месяц (число от 0 до 12):")
    month = get_correct_input(lambda x: x.isdigit() and (1 <= int(x) <= 12))
    print("Введите день: ")
    day = get_correct_input(lambda x: day_is_correct(x, month, year))

    return datetime.strptime(f'{day}/{month}/{year}', '%d/%m/%Y')


def get_multiline_input() -> str:
    print('введите пустую строку для завершения ввода:')
    output = ''
    new_line = input()
    while new_line != '':
        output += new_line + '\n'
        new_line = input()
    return output
