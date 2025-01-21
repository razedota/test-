телефонна_книга= {

}

def add_contact():

    name = input("Введіть ім'я контакту: ").strip()
    phone = input("Введіть номер телефону: ").strip()
    if name in phone_book:
        print("Контакт з таким ім'ям вже існує.")
    else:
        phone_book[name] = phone
        print(f"Контакт {name} додано.")


def find_contact():

    name = input("Введіть ім'я для пошуку: ").strip()
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print("Контакт не знайдено.")


def delete_contact():

    name = input("Введіть ім'я для видалення: ").strip()
    if name in phone_book:
        del phone_book[name]
        print(f"Контакт {name} видалено.")
    else:
        print("Контакт не знайдено.")


def main():

    while True:

        print("\nТелефонна книга")
        print("1. Додати контакт")
        print("2. Знайти контакт")
        print("3. Видалити контакт")
        print("4. Вихід")

        choice = input("Виберіть дію (1-4): ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            find_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            print("Програма завершена.")
        not true
    else:
            print("Некоректний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()