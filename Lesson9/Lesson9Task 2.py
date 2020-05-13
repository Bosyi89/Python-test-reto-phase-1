
"""1. відкрити (створити) файл
2. Якщо файлу неіснує то показати помилку і написати про це користувачу
3. Читати json файл
4. якщо під час читання з'являється помилка то незвертати увагу і продовжувати
5. Зберегти файл
6. Меню друку
7. якщо користувач вибрав, додайте новий запис:
   1. Попросіть користувача ввести дані
   2. Додайте дані до списку
8. якщо користувач обрав запис пошуку / видалення:
"""

import json


json_file = open('New_file') as New_file:

try:
    myphonebook = json.load(json_file)
except json.decoder.JSONDecodeError:
    myphonebook = []
json_file.close()

dict_pattern = {
    'first_name': '',
    'last_name': '',
    'full_name': '',
    'phone': '',
    'region': '',
    'city': ''
}

try:
    while True:
        command = input('Select command: ').strip().lower()
        if command == 'add':
            first_name = input('Enter first name: ').strip().lower().title()
            last_name = input('Enter last name: ').strip().lower().title()
            full_name = first_name + ' ' + last_name
            phone = input('Enter phone: ')
            region = input('Enter region: ').strip().lower().title()
            city = input('Print city: ').strip().lower().title()
            new_dict = dict_pattern.copy()
            new_dict['first_name'] = first_name
            new_dict['last_name'] = last_name
            new_dict['full_name'] = full_name
            new_dict['phone'] = phone
            new_dict['region'] = region
            new_dict['city'] = city
            myphonebook.append(new_dict)
        elif command == 'search first name':
            query = input('First name: ').strip().lower().title()
            for item in myphonebook:
                if item['first_name'] == query:
                    print('Found person:')
                    print(item)
                    break
        elif command == 'search last name':
            query = input('Last name: ').strip().lower().title()
            for item in myphonebook:
                if item['last_name'] == query:
                    print('Found person:')
                    print(item)
                    break
        elif command == 'search full name':
            query = input('Full name: ').strip().lower().title()
            for item in myphonebook:
                if item['full_name'] == query:
                    print('Found person:')
                    print(item)
                    break
        elif command == 'search phone':
            query = input('Phone: ')
            for item in myphonebook:
                if item['phone'] == query:
                    print('Found person:')
                    print(item)
                    break
        elif command == 'search city':
            query = input('City: ').strip().lower().title()
            for item in myphonebook:
                if item['city'] == query:
                    print('Found person:')
                    print(item)
                    break
        elif command == 'search region':
            query = input('Region: ').strip().lower().title()
            for item in myphonebook:
                if item['region'] == query:
                    print('Found person:')
                    print(item)
                    break
        elif command == 'exit':
            break
        elif command == 'update':
            query = input('Phone: ')
            for item in myphonebook:
                if item['phone'] == query:
                    phb.remove(item)
                    first_name = input('Enter first name: ').strip().lower().title()
                    last_name = input('Enter last name: ').strip().lower().title()
                    full_name = first_name + ' ' + last_name
                    phone = input('Enter phone: ')
                    region = input('Enter region: ').strip().lower().title()
                    city = input('Print city: ').strip().lower().title()
                    new_dict = dict_pattern.copy()
                    new_dict['first_name'] = first_name
                    new_dict['last_name'] = last_name
                    new_dict['full_name'] = full_name
                    new_dict['phone'] = phone
                    new_dict['region'] = region
                    new_dict['city'] = city
                    phb.append(new_dict)
                    break
        elif command == 'delete':
            query = input('Phone: ')
            for item in myphonebook:
                if item['phone'] == query:
                    myphonebook.remove(item)
                    break


except Exception as e:
    print('Erorr')
    print(e)
finally:
    with open('myphonebook.json', 'w') as json_file:
        json.dump(myphonebook, json_file, indent=4)