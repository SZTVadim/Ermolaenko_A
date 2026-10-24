# Задание 1. Работа с типами данных
text = "Привет"
number = 42
float_number = 3.14
numbers = [1, 2, 3]

print(type(text))
print(type(number))
print(type(float_number))
print(type(numbers))

# Задание 2. Преобразование регистра строк
text = "python PROGRAMMING"

print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.title())

# Задание 3. Удаление пробелов
text = "  Hello World  "

print(text.strip())
print(text.lstrip())
print(text.rstrip())

# Задание 4. Разделение и объединение строк
text = "яблоко,банан,апельсин,груша"

fruits = text.split(",")
print(fruits)

new_text = " | ".join(fruits)
print(new_text)

# Задание 5. Замена подстрок
text = "Я изучаю Python. Python - это круто!"

new_text = text.replace("Python", "Java")
print(new_text)

# Задание 6. Поиск и подсчет
text = "Python программирование на Python"

print(text.index("Python"))
print(text.count("Python"))
print(text.find("Java"))

# Задание 7. Проверка типа символов
print("Hello123".isalnum())
print("12345".isdigit())
print("Hello".isalpha())
print("   ".isspace())

# Задание 8. Срезы строк
text = "Python very good"

print(text[0:3])
print(text[-3:])
print(text[::2])
print(text[::-1])

# Задание 9. Экранирование символов
print("Он сказал: \"Привет\"")
print("Первая строка\nВторая строка")
