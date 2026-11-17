# Задание 1. Функции и условия
def calculate_total(price, tax_percent):
    if tax_percent > 20 or price < 0:
        result = "Ошибка в данных"
    else:
        result = price + price * tax_percent / 100
    return result


def get_level(points):
    if points >= 100:
        result = "Эксперт"
    elif points >= 50:
        result = "Продвинутый"
    elif points >= 20:
        result = "Начинающий"
    else:
        result = "Новичок"
    return result


# Задание 2. Функции с условиями и match/case
def process_status(status):
    match status:
        case "active":
            result = "Статус активен"
        case "inactive":
            result = "Статус неактивен"
        case "pending":
            result = "Статус в ожидании"
        case "blocked":
            result = "Статус заблокирован"
        case _:
            result = "Неизвестный статус"
    return result
