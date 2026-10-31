# Задание 1. Работа со словарями и перебор элементов
student = {
    "имя": "Иван",
    "возраст": 20,
    "курс": 2,
    "город": "Москва",
}

print(student.keys())
print(student.values())

for key, value in student.items():
    print(f"{key}: {value}")

for value in student.values():
    print(value)

# Задание 2. Удаление элементов и генератор словарей
prices = {
    "яблоко": 50,
    "банан": 30,
    "апельсин": 40,
    "груша": 35,
    "виноград": 60,
}

del prices["груша"]
price_grape = prices.pop("виноград")

discount_prices = {key: value * 0.9 for key, value in prices.items()}
print(discount_prices)

# Задание 3. Объединение словарей
student1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}

student1.update(student2)
print(student1)

student3 = student1.copy()
student3.update(student2)

print(student1)
print(student2)
print(student3)
