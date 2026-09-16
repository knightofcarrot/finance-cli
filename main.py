from storage import load_data, save_data
from finance import (
    add_transaction,
    get_balance,
    add_category,
    remove_category,
    get_month_statistics,
    get_category_statistics
)


def show_menu():
    print("\nЛичные финансы")
    print("1. Добавить доход")
    print("2. Добавить расход")
    print("3. Посмотреть баланс")
    print("4. Добавить категорию")
    print("5. Удалить категорию")
    print("6. Показать категории")
    print("7. Статистика за месяц")
    print("8. Статистика расходов по категориям")
    print("0. Выход")


def get_amount():
    try:
        amount = float(input("Введите сумму: "))

        if amount <= 0:
            print("Сумма должна быть больше нуля.")
            return None

        return amount

    except ValueError:
        print("Сумма должна быть числом.")
        return None


def get_category(data):
    if not data["categories"]:
        print("Список категорий пуст.")
        return None

    print("Категории:")

    for category in data["categories"]:
        print("-", category)

    category_name = input("Введите категорию: ").strip()

    for category in data["categories"]:
        if category.lower() == category_name.lower():
            return category

    print("Такой категории нет.")
    return None


def get_month():
    month = input("Введите месяц в формате ММ.ГГГГ: ").strip()
    parts = month.split(".")

    if len(parts) != 2:
        print("Неверный формат.")
        return None

    if not parts[0].isdigit() or not parts[1].isdigit():
        print("Неверный формат.")
        return None

    if len(parts[0]) != 2 or len(parts[1]) != 4:
        print("Неверный формат.")
        return None

    month_number = int(parts[0])

    if month_number < 1 or month_number > 12:
        print("Неверный формат.")
        return None

    return month


def main():
    data = load_data()

    while True:
        show_menu()
        choice = input("Выберите действие: ").strip()

        if choice == "0":
            save_data(data)
            print("Данные сохранены.")
            print("До свидания!")
            break

        elif choice == "1":
            amount = get_amount()

            if amount is not None:
                category = get_category(data)

                if category is not None:
                    description = input("Введите описание: ").strip()

                    add_transaction(
                        data,
                        "income",
                        amount,
                        category,
                        description
                    )

                    save_data(data)
                    print("Доход добавлен.")

        elif choice == "2":
            amount = get_amount()

            if amount is not None:
                category = get_category(data)

                if category is not None:
                    description = input("Введите описание: ").strip()

                    add_transaction(
                        data,
                        "expense",
                        amount,
                        category,
                        description
                    )

                    save_data(data)
                    print("Расход добавлен.")

        elif choice == "3":
            balance = get_balance(data)

            print("\nТекущий баланс")
            print("Доходы:", balance["income"])
            print("Расходы:", balance["expense"])
            print("Баланс:", balance["balance"])

        elif choice == "4":
            category = input("Введите название категории: ").strip()

            if add_category(data, category):
                save_data(data)
                print("Категория добавлена.")
            else:
                print("Категория не добавлена. Возможно, она уже существует.")

        elif choice == "5":
            category_name = input("Введите название категории: ").strip()
            category_to_remove = None

            for category in data["categories"]:
                if category.lower() == category_name.lower():
                    category_to_remove = category
                    break

            if category_to_remove is None:
                print("Категория не найдена.")
            elif remove_category(data, category_to_remove):
                save_data(data)
                print("Категория удалена.")

        elif choice == "6":
            if data["categories"]:
                print("\nКатегории:")

                for category in data["categories"]:
                    print("-", category)
            else:
                print("Список категорий пуст.")

        elif choice == "7":
            month = get_month()

            if month is not None:
                statistics = get_month_statistics(data, month)

                print("\nСтатистика за", month)
                print("Доходы:", statistics["income"])
                print("Расходы:", statistics["expense"])
                print("Баланс:", statistics["balance"])

        elif choice == "8":
            month = get_month()

            if month is not None:
                statistics = get_category_statistics(data, month)

                if statistics:
                    print("\nРасходы по категориям за", month)

                    for category, amount in statistics.items():
                        print(category + ":", amount)
                else:
                    print("Расходов за этот месяц нет.")

        else:
            print("Такого пункта меню нет.")


if __name__ == "__main__":
    main()