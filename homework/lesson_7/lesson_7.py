# Задание 1. Работа с множествами
fruits = {"яблоко", "банан"}

fruits.add("апельсин")
fruits.update(["груша", "виноград"])
fruits.discard("банан")
fruits.discard("киви")
# fruits.remove("киви")
random_fruit = fruits.pop()
print(fruits)

# Задание 2. Работа с кортежами
coordinates = (10, 20, 30, 20, 10, 20, 40)

print(coordinates[0])
print(coordinates[-1])
print(coordinates[1:4])
30 in coordinates
coordinates.index(20)
coordinates.count(20)
coordinates.count(50)
print(len(coordinates))
