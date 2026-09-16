from datetime import datetime
def add_transaction(data: dict, trans_type: str, amount: float, category: str, description: str = ""):
    if data["transactions"]:
        new_id = max(t["id"] for t in data["transactions"]) + 1
    else:
        new_id = 1

    transaction = {
        "id": new_id,
        "type": trans_type,  #income или expense
        "amount": round(amount, 2),
        "category": category,
        "date": datetime.now().strftime("%d.%m.%Y"),
        "description": description
    }

    data["transactions"].append(transaction)
    return data

def get_balance(data: dict):

    total_income = 0
    for t in data["transactions"]:
        if t["type"] == "income":
            total_income += t["amount"]

    total_expense = 0
    for t in data["transactions"]:
        if t["type"] == "expense":
            total_expense += t["amount"]
    
    return {
        "income": round(total_income, 2),
        "expense": round(total_expense, 2),
        "balance": round(total_income - total_expense, 2)
    }

def add_category(data: dict, category_name: str):
    cleaned_name = category_name.strip()
    if cleaned_name and cleaned_name not in data["categories"]:
        data["categories"].append(cleaned_name)
        return True
    return False

def remove_category(data: dict, category_name: str):
    cleaned_name = category_name.strip()
    if cleaned_name in data["categories"]:
        data["categories"].remove(cleaned_name)
        return True
    return False

def get_month_statistics(data: dict, month: str):
    total_income = 0
    total_expense = 0

    for transaction in data["transactions"]:
        if transaction["date"][3:] == month:
            if transaction["type"] == "income":
                total_income += transaction["amount"]
            elif transaction["type"] == "expense":
                total_expense += transaction["amount"]

    return {
        "income": round(total_income, 2),
        "expense": round(total_expense, 2),
        "balance": round(total_income - total_expense, 2)
    }

def get_category_statistics(data: dict, month: str):
    statistics = {}

    for transaction in data["transactions"]:
        if transaction["date"][3:] == month and transaction["type"] == "expense":
            category = transaction["category"]

            if category not in statistics:
                statistics[category] = 0

            statistics[category] += transaction["amount"]

    for category in statistics:
        statistics[category] = round(statistics[category], 2)

    return statistics