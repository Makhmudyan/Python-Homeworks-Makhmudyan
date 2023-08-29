# Задача 38: Дополнить телефонный справочник возможностью изменения и
# удаления данных. Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных

def delete(phonebook, delete_contact):
    filename = 'contactss.txt'
    deleted_contact = []
    for contact in phonebook:
        if contact['last_name'].lower().strip() == delete_contact.lower().strip() or contact['first_name'].lower().strip() == delete_contact.lower().strip():
            deleted_contact.append(contact)


    if deleted_contact:
        for contact in deleted_contact:
            phonebook.remove(contact)
            print(f"Контакт {delete_contact} успешно удален\n")
            save_to_file(filename, phonebook)
        else:
            print(f'Контакт {delete_contact} не найден\n')

def edit(phonebook, edit_contact):
    filename = 'contactss.txt'
    edited_contact = []
    for contact in phonebook:
        if (contact['last_name'].lower() == edit_contact.lower() or contact['first_name'].lower().strip() == edit_contact.lower()):
            edited_contact.append(contact)
            print(f'{edited_contact}')
        

    if edited_contact:
        edit = input("Введите действие:\n 1.Изменить имя\n 2.Изменить фамилию\n 3.Изменить отчество\n 4.Изменить номер телефона\n")
        while True:
            if edit == '1':
                edit_first_name = input('Введите новое имя: ')
                contact['first_name'] = edit_first_name
                print(f'Имя успешно изменено\n')
                save_to_file(filename, phonebook)
                break
            elif edit == '2':
                edit_last_name = input('Введите новою фамилию: ')
                contact['last_name'] = edit_last_name
                print(f'Фамилия успешна изменена\n')
                save_to_file(filename, phonebook)
                break
            elif edit == '3':
                edit_middle_name = input('Введите новое отчество: ')
                contact['middle_name'] = edit_middle_name
                print(f'Отчество успешно изменено\n')
                save_to_file(filename, phonebook)
                break           
            elif edit == '4':
                edit_phone_number = input('Введите новый номер телефона: ')
                contact['phone_number'] = edit_phone_number
                print(f'Номер телефона успешно изменен\n')
                save_to_file(filename, phonebook)
                break
            else:
                print('Некорректный выбор. Попробуйте снова\n')
                break 
    else:
            print(f'Контакт {edit_contact} не найден!\n')  
        

def load_file(filename):
    phonebook = []
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            for contact in file:
                last_name, first_name, middle_name, phone_number = contact.split(',')
                phonebook.append({
                    'last_name': last_name.strip(),
                    'first_name': first_name.strip(),
                    'middle_name': middle_name.strip(),
                    'phone_number': phone_number.strip()
                })
            print('Данные успешно загружены\n')
    except FileNotFoundError:
        print('Файл не найден\n')
    return phonebook

def search_contacts(phonebook, search_key):
    results = []
    for contact in phonebook:
        if(search_key.lower() in contact['last_name'].lower() or search_key.lower() in contact['first_name'].lower()):
            results.append(contact)
    return results

def view_contacts(phonebook):
    for index, contact in enumerate(phonebook, start=1):
        print(f"{index}. {contact['last_name']}, {contact['first_name']}, {contact['middle_name']}, {contact['phone_number']}")


def save_to_file(filename, phonebook):
    with open(filename, 'w', encoding="utf-8") as file:
        for contact in phonebook:
            file.write(f"{contact['last_name']}, {contact['first_name']}, {contact['middle_name']}, {contact['phone_number']}\n")
    print('Данные сохранены в файле\n')

def add_contact(phonebook, last_name, first_name, middle_name, phone_number):
    contact = {
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'phone_number': phone_number
    }
    phonebook.append(contact)
    print('Контакт добавлен')

def main():
    filename = 'contactss.txt'
    phonebook = []

    while True:
        print("1. Добавить контакт")
        print("2. Сохранить файл")
        print("3. Вывести все контакты")
        print("4. Поиск по имени/фамилии")
        print("5. Загрузить из файла")
        print("6. Удалить контакт")
        print("7. Изменить контакт")
        print("8. Выйти")
        
        choice = input("Выберите действие: ")
        if choice == '1':
            last_name = input('Фамилия: ')
            first_name = input('Имя: ')
            middle_name = input('Отчество: ')
            phone_number = input('Номер телефона: ')
            add_contact(phonebook, last_name, first_name, middle_name, phone_number)
        elif choice == '2':
            save_to_file(filename, phonebook)
        elif choice == '3':
            view_contacts(phonebook)
        elif choice == '4':
            search_key = input("Введите имя или фамилию для поиска: ")
            results = search_contacts(phonebook, search_key)
            if(results):
                print('Найдены контакты: ')
                print(results)
            else:
                print('Контактов по вашему запросу нет!')
        elif choice == '5':
            phonebook = load_file(filename)
        elif choice == '6':
            delete_contact = input('Введите имя или фамилию контакта, который хотите удалить: ')
            delete(phonebook, delete_contact)
        elif choice == '7':
            edit_contact = input('Введите имя или фамилию контакта, который хотите изменить: ')
            edit(phonebook, edit_contact)
        elif choice == '8':
            break
        else:
            print('Некорректный выбор. Попробуйте снова')
        

if __name__ == "__main__":
    main()
