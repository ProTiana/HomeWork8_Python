def creating ():
    file = 'Phonebook.csv'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Фамилия;Имя;Дата рождения;Номер телефона;Описание\n')
