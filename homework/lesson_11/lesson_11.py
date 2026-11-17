# Задание 1. Класс Book
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"'{self.title}' автор {self.author}, {self.pages} стр."

    def is_long(self):
        if self.pages > 300:
            return True
        else:
            return False


book1 = Book("Книга первая", "Автор первый", 74)
book2 = Book("Книга вторая", "Автор второй", 300)
book3 = Book("Книга третья", "Автор третий", 450)

print(book1.get_info())
print(book2.get_info())
print(book3.get_info())


# Задание 2. Класс BankAccount
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            result = True
        else:
            print("Недостаточно средств")
            result = False
        return result

    def get_balance(self):
        return self.balance


account = BankAccount("Ермолаенко А.С.")
account.deposit(1000)

print(account.withdraw(400))
print(account.withdraw(700))
print(account.get_balance())
