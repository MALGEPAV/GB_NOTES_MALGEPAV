from command_processing import *

print("НАЧАЛО РАБОТЫ")

command = ''
while command != '0':
    main_menu_command_handler(command)
    command = main_menu_command()

print('ЗАВЕРШЕНИЕ РАБОТЫ')
0
