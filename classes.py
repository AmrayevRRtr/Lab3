ex1
class String:
  def getString(self):
    self.s=str(input())
  def printString(self):
    print(self.s.upper())
p1=String()
p1.getString()
p1.printString()
ex2
class Shape:
    def area(self):
        self.a=0
        print ("area: ", self.a)
class Square(Shape):
    def __init__(self):
        self.length=float(input("length: "))
    def area(self):
        a=self.length**2
        print("area: ",a)

p1=Shape()
p1.area()

p2=Square()
p2.area()
ex3
class Shape:
    def area(self):
        self.a=0
        print ("area: ", self.a)
class Rectangle(Shape):
    def __init__(self):
        self.length=float(input("length: "))
        self.width=float(input("width: "))
    def area(self):
        a=self.length*self.width
        print("area: ", a)
p1=Shape()
p1.area()

p2=Rectangle()
p2.area()
ex4
import math
class point:
    def show(self):
        self.x1=int(input("x1= "))
        self.y1=int(input("y1= "))
    def move(self):
        self.x2=int(input("x2= "))
        self.y2=int(input("y2= "))
    def dist(self):
        self.AB=math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
        print("distance= ", self.AB)

p1=point()
p1.show()
p1.move()
p1.dist()
ex5
class Account:
    def __init__(self):
        self.owner=str(input("���: "))
        self.balance=0
    def deposit(self):
        self.amount=int(input("������� �����: "))
        self.balance+=self.amount
        print("����������: ", self.balance, "\n��������:", self.balance)
    def widthdrawals(self):
        self.amount=int(input("������� ����� ��� ������: "))
        if self.amount<=self.balance:
            self.balance-=self.amount
            print("�� ������� ����� �����.")
            print ("��������:", self.balance)
        else:
            print("� ��� ������������ �������.")

p1=Account()
p1.deposit()
p1.widthdrawals()
ex6
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers:", prime_numbers)