from abc import ABC, abstractmethod

# ==========================================
# Task 1
# ==========================================
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Balance:", self.balance)
        else:
            print("Insufficient funds")

    def check_balance(self):
        print("Balance:", self.balance)


# ==========================================
# Task 2
# ==========================================
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height


# ==========================================
# Task 3
# ==========================================
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    def to_kelvin(self):
        return self.celsius + 273.15


# ==========================================
# Task 4
# ==========================================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("name is", self.name)
        print("age is", self.age)


class Employee(Person):
    def __init__(self, name, age, salary, job_title):
        super().__init__(name, age)
        self.salary = salary
        self.job_title = job_title

    def give_raise(self, percentage):
        self.salary += self.salary * percentage / 100
        print("New salary:", self.salary)


# ==========================================
# Task 5
# ==========================================
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class RectangleShape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def calculate_area(shape):
    print(shape.area())


# ==========================================
# Task 6
# ==========================================
class MathOperations:
    def calculate(self, a, b, c=0):
        return a + b + c


# ==========================================
# Task 7
# ==========================================
class PasswordManager:
    def __init__(self):
        self._password = ""

    def set_password(self, password):
        if len(password) < 8:
            print("Password too short")
        else:
            self._password = password
            print("Password set")

    def verify(self, input_password):
        return input_password == self._password


# ==========================================
# Task 9
# ==========================================
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        return "This is a shape"


class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# ==========================================
# Task 10
# ==========================================
class AbstractEmployee(ABC):
    @property
    @abstractmethod
    def salary(self):
        pass

    @abstractmethod
    def calculate_bonus(self):
        pass


class Manager(AbstractEmployee):
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    def calculate_bonus(self):
        return self.salary * 20 / 100