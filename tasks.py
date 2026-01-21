from datetime import datetime, timedelta
from utils import parse_datetime, format_datetime, validate_status, get_status_priority

def load_tasks(filename="tasks_data.txt"):
    tasks = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                parts = line.split(";")
                assign_dt_str, due_dt_str, executor, desc, status = parts
                tasks.append({
                    "assign_datetime": parse_datetime(assign_dt_str),
                    "due_datetime": parse_datetime(due_dt_str),
                    "executor": executor,
                    "description": desc,
                    "status": status
                })
    except FileNotFoundError:
        print(f'Файл {filename} не найден. Создайте его или проверьте путь.')
        return []
    return tasks

def shell_sort(arr, key_func):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and key_func(arr[j - gap]) > key_func(temp):
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def filter_tasks_by_days(tasks, n_days):
    now = datetime.now()
    start_date = now - timedelta(days=n_days)
    return [t for t in tasks if t["assign_datetime"] >= start_date]

def filter_tasks_by_executor_and_status(tasks, executor, target_status):
    return [t for t in tasks if t["executor"].lower() == executor and t["status"] == target_status]

def filter_active_tasks(tasks):
    active_statuses = {"получена", "в процессе"}
    return [t for t in tasks if t["status"] in active_statuses]

def report1_key(task):
    #функция для создания кортежа для сравнения значений в сортировке
    #для отчёта 1 по дате получения и статусу задачи
    return (
        -task["assign_datetime"].timestamp(),
        get_status_priority(task["status"])
    )

def generate_report_1(tasks, n_days):
    filtered = filter_tasks_by_days(tasks, n_days)
    shell_sort(filtered, key_func=report1_key)
    return filtered

def report2_key(task):
    #функция для создания кортежа для сравнения значений в сортировке
    #для отчёта 2 по предполагаемой дате выполнения и описанию
    return (
        -task["due_datetime"].timestamp(),
        task["description"]
    )

def generate_report_2(tasks, executor):
    filtered = filter_tasks_by_executor_and_status(tasks, executor, "провалена")
    shell_sort(filtered, key_func=report2_key)
    return filtered

def report3_key(task):
    #функция для создания кортежа для сравнения значений в сортировке
    #для отчёта 3 по исполнителю и предполагаемой дате выполнения
    return (
        task["executor"],
        task["due_datetime"].timestamp()
    )

def generate_report_3(tasks):
    filtered = filter_active_tasks(tasks)
    shell_sort(filtered, key_func=report3_key)
    return filtered

def print_tasks(tasks):
    if not tasks:
        print("Нет задач для отображения.")
        return
    print(f"\n{'Дата получения':<18} {'Дата выполнения':<18} {'Исполнитель':<12} {'Статус':<18} Описание")
    print("-" * 80)
    for t in tasks:
        print(
            f"{format_datetime(t['assign_datetime']):<18} "
            f"{format_datetime(t['due_datetime']):<18} "
            f"{t['executor']:<12} "
            f"{t['status']:<18} "
            f"{t['description']} "
        )