# Задание 1. Добавление элементов в список
fruits = ["яблоко"]

fruits.append("банан")
fruits.extend(["апельсин", "груша"])
fruits.insert(1, "виноград")

# Задание 2. Удаление элементов из списка
fruits = ["яблоко", "банан", "апельсин", "банан"]

fruits.remove("банан")
my_var = fruits.pop()

# Задание 3. Поиск элементов в списке
fruits = ["яблоко", "банан", "апельсин", "банан"]

fruits.index("банан")
fruits.count("банан")

# Задание 4. Сортировка и реверс списка
numbers = [3, 1, 4, 1, 5, 9, 2]

numbers.sort()
numbers.reverse()
print(numbers)

# Задание 5.
cubes = [x ** 3 for x in range(1, 9)]

print(min(cubes))
print(max(cubes))

# Задание 6.
numbers = [5, 12, 8, 15, 3, 20, 7, 18, 9, 11]
filtered_numbers = [x for x in numbers if x > 10]

print(sum(filtered_numbers))

# Задание 7.
cities = ["москва", "санкт-петербург", "казань"]
update_cities = [city.title() for city in cities]

print(update_cities)
