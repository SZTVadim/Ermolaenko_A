# Задание: Система управления животными в зоопарке

# Часть 1: Абстракция - Абстрактный класс Animal

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Часть 2: Наследование - Классы Dog и Cat


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Гав-гав!")


class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Мяу!")

# Часть 3: Инкапсуляция - класс Zoo


class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def get_animals_count(self):
        return len(self.__animals)

    def get_animals(self):
        return self.__animals.copy()


# Часть 4: Полиморфизм - работа с разными животными


def animal_sound(animal):
    # это полиморфизм, т.к. дна функция работает с разными животными.
    # Каждый класс реализует make_sound() по-своему.
    animal.make_sound()


dog1 = Dog("Бобик", 3)
dog2 = Dog("Шарик", 5)
cat1 = Cat("Мурка", 2)

zoo = Zoo("Городской зоопарк")

zoo.add_animal(dog1)
zoo.add_animal(dog2)
zoo.add_animal(cat1)

print(zoo.get_animals_count())

for animal in zoo.get_animals():
    animal_sound(animal)

# Часть 4.11

# animal = Animal()
# при попытке создать объект возникает TypeError.
# нельзя создать объект класса с нереализованным абстрактным методом.
# классы Dog и Cat реализуют make_sound(), поэтому их объекты создавать можно.
