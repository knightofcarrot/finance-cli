from storage import load_data, save_data

data = load_data()
print("Исходные данные:", data)

data["categories"].append("Кино")
data["transactions"].append({
    "id": 1,
    "type": "expense",
    "amount": 500,
    "category": "Еда",
    "date": "15.09.2026"
})

save_result = save_data(data)
print("Сохранение прошло успешно?:", save_result)

reloaded_data = load_data()
print("Прочитанные данные из файла:", reloaded_data)