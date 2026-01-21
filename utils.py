from datetime import datetime

def parse_datetime(dt_str):
    """Преобразует строку вида 'YYYY-MM-DD HH:MM' в объект datetime."""
    return datetime.strptime(dt_str, "%Y-%m-%d %H:%M")

def format_datetime(dt_obj):
    """Форматирует datetime в читаемую строку."""
    return dt_obj.strftime("%d.%m.%Y %H:%M")

def validate_status(status):
    valid = {"получена", "в процессе", "успешно выполнена", "провалена"}
    return status in valid

def get_status_priority(status):
    order = {
        "провалена": 3,
        "получена": 2,
        "в процессе": 1,
        "успешно выполнена": 0
    }
    return order.get(status, 99)