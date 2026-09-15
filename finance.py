from datetime import datetime
def add_transaction(data: dict, trans_type: str, amount: float, category: str, description: str = ""):
    if len(data["transactions"]) > 0:
        new_id = len(data["transactions"]) + 1
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
        "income": total_income,
        "expense": total_expense,
        "balance": total_income - total_expense
    }

def add_category(data: dict, category_name: str):
    if category_name not in data["categories"]:
        data["categories"].append(category_name)
        return True
    return False

def remove_category(data: dict, category_name: str):
    if category_name in data["categories"]:
        data["categories"].remove(category_name)
        return True
    return False