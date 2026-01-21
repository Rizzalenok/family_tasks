from tasks import load_tasks, generate_report_1, generate_report_2, generate_report_3, print_tasks

def input_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Значение должно быть ≥ {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Значение должно быть ≤ {max_val}")
                continue
            return value
        except ValueError:
            print("Введите корректное число.")

def input_executor():
    while True:
        name = input("Введите имя исполнителя (мама/папа/Анна): ").strip().lower()
        if name:
            return name
        print("Имя не может быть пустым.")

def main():
    tasks = load_tasks()
    if not tasks:
        print("Невозможно загрузить задачи. Программа завершена.")
        return

    while True:
        print("\nСЕМЕЙНЫЙ МЕНЕДЖЕР ЗАДАЧ")
        print("\n1. Отчёт 1: Задачи за последние N дней")
        print("2. Отчёт 2: Проваленные задачи конкретного члена семьи")
        print("3. Отчёт 3: Все активные задачи")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            n = input_int("Введите количество дней (N ≥ 1): ", min_val=1, max_val=365)
            report = generate_report_1(tasks, n)
            print(f"\nОтчёт 1: Задачи за последние {n} дн.")
            print_tasks(report)

        elif choice == "2":
            executor = input_executor()
            report = generate_report_2(tasks, executor)
            print(f"\nОтчёт 2: Проваленные задачи '{executor}'")
            print_tasks(report)

        elif choice == "3":
            report = generate_report_3(tasks)
            print("\nОтчёт 3: Все активные задачи")
            print_tasks(report)

        elif choice == "0":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()