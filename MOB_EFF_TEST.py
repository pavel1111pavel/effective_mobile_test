import os


# Функция для добавления новой записи в справочник
def add_entry(entries):
    entry = {}
    entry['last_name'] = input("Фамилия: ")
    entry['first_name'] = input("Имя: ")
    entry['middle_name'] = input("Отчество: ")
    entry['organization'] = input("Организация: ")
    entry['work_phone'] = input("Рабочий телефон: ")
    entry['personal_phone'] = input("Личный телефон: ")
    entries.append(entry)


# Функция для вывода записей на экран
def display_entries(entries, page_size=5):
    total_entries = len(entries)
    num_pages = (total_entries + page_size - 1) // page_size

    for page in range(num_pages):
        start_idx = page * page_size
        end_idx = min((page + 1) * page_size, total_entries)
        print("\nСтраница", page + 1)
        for idx in range(start_idx, end_idx):
            entry = entries[idx]
            print("Фамилия:", entry['last_name'])
            print("Имя:", entry['first_name'])
            print("Отчество:", entry['middle_name'])
            print("Организация:", entry['organization'])
            print("Рабочий телефон:", entry['work_phone'])
            print("Личный телефон:", entry['personal_phone'])
            print("-" * 30)


# Функция для сохранения записей в файл
def save_to_file(entries, filename):
    with open(filename, 'w') as file:
        for entry in entries:
            file.write(f"{entry['last_name']},{entry['first_name']},{entry['middle_name']},"
                       f"{entry['organization']},{entry['work_phone']},{entry['personal_phone']}\n")


# Загрузка записей из файла
def load_from_file(filename):
    entries = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                entry = {
                    'last_name': parts[0],
                    'first_name': parts[1],
                    'middle_name': parts[2],
                    'organization': parts[3],
                    'work_phone': parts[4],
                    'personal_phone': parts[5]
                }
                entries.append(entry)
    return entries


def main():
    filename = 'phonebook.txt'
    entries = load_from_file(filename)

    while True:
        print("\nМеню:")
        print("1. Вывод записей")
        print("2. Добавление записи")
        print("3. Сохранить и выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            display_entries(entries)
        elif choice == '2':
            add_entry(entries)
        elif choice == '3':
            save_to_file(entries, filename)
            print("Данные сохранены. Программа завершена.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите снова.")


if __name__ == "__main__":
    main()
