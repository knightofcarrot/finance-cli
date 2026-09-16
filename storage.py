import json
import os 

DATA_FILE = "finance_data.json"

DEFAULT_DATA = {
    "categories": ["Еда", "Зарплата", "Такси"], #тупо заглушка на 1 раз
    "transactions":[]
}

def load_data(file_path: str = DATA_FILE):
    if not os.path.exists(file_path):
        return DEFAULT_DATA.copy()
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Загружена пустая база")
        return DEFAULT_DATA.copy()

def save_data(data: dict, file_path: str = DATA_FILE):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except OSError as e:
        print(f"Ошибка при сохранении данных: {e}")
        return False