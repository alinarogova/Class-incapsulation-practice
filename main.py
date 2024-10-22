from random import randint
print("Task 1".center(60, "="))


class Person:
    n = 0

    def __init__(self, firstname, lastname, age):
        self.firstName = firstname
        self.lastName = lastname
        self._age = age
        Person.n += 1
        self.__personID = randint(1, 100)

    def getInfo(self):
        return (f"Person first name - {self.firstName}, "
                f"last name - {self.lastName}, "
                f"age - {self._age}, "
                f"ID - {self.__personID}")

    def getHi(self, msgText="Hi"):
        persInf = self.getInfo()
        return f"{persInf}\n {msgText}! I am {self.firstName}"

    def __getID(self):
        return f"{self.__personID}"

    def _getFullName(self):
        return f"Full name: {self.firstName} {self.lastName}"

    @staticmethod
    def count_persons():
        return Person.n


per1 = Person("Vasya", "Kolyada", 24)
per2 = Person("Margo", "Robbie", 30)
per2 = Person("Margo", "Robbie", 30)
print(Person.count_persons())
print("Task 2".center(60, "="))


class Square:
    n = 0

    @staticmethod
    def triangleSquare1(a, h):
        Square.n += 1
        return a*h/2

    @staticmethod
    def triangleSquare2(a, b, c):
        Square.n += 1
        p = (a+b+c)/2
        return (p*(p-a)*(p-b)*(p-c)) ** 0.5

    @staticmethod
    def rectangleSquare(a, b):
        Square.n += 1
        return a*b

    @staticmethod
    def areaSquare(a):
        Square.n += 1
        return a ** 2

    @staticmethod
    def rhombSquare(d1, d2):
        Square.n += 1
        return d1 * d2/2

    @staticmethod
    def count_classes():
        return Square.n


print(Square.triangleSquare1(5, 7))
print(Square.triangleSquare2(5, 7, 8))
print(Square.rectangleSquare(5, 7))
print(Square.areaSquare(5))
print(Square.rhombSquare(5, 7))
print(Square.count_classes())

print("Task 3".center(60, "="))


class Calc:
    @staticmethod
    def max4(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def min4(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def avg4(a, b, c, d):
        return (a+b+c+d)/4

    @staticmethod
    def fact(a):
        res = 1
        if a < 0:
            print("Invalid argument!")
            return
        for i in range(int(a)):
            res *= i
        return res


print("max", Calc.max4(3, 4, -9, 1))
print("min", Calc.min4(3, 4, -9, 1))
print("avg", Calc.avg4(3, 4, -9, 1))
print("factorial", Calc.fact(5))
