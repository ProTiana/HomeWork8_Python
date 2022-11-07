from view_interface import get_info as view

info = view()
def writing_scv ():
    file = 'Phonebook.csv'
    with open(file, 'w', encoding ='utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]};{info[4]}\n')

def writing_txt ():
    file = 'Phonebook.txt'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nДата рождения: {info[2]}\n\nНомер телефона: {info[3]}\n\nОписание: {info[4]}\n\n\n')