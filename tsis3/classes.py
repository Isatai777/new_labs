#ex1
class StringManipulator:

    def getString(self):
        self.input_string = input(" ")

    def printString(self):
        print(self.input_string.upper())

l1 = StringManipulator()
l1.getString()
l1.printString()

#ex2 
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width =width
    def area(self):
        return self.length*self.width
is_rect = input("Is this a rectangle? Answer: Y/N ")
if is_rect == "Y":
    length =float(input(" "))
    width = float(input(" "))
    print(Rectangle(length,width).area())
else:
    print(Shape().area())

#ex4 
import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        return (self.x, self.y)
    def get_dist(self, x2,y2):
        self.x2 =x2
        self.y2 =y2
        self.dist =math.sqrt((self.x2-self.x)**2 + (self.y2 - self.y)**2)
        return "The distance between 2 points is " + str(round(self.dist,2))
    def move(self, new_x, new_y):
         self.new_x = new_x
         self.new_y = new_y
         print("The first coordinates was: ")
         print("(", self.x, self.y,")")
         self.x = self.new_x
         self.y = self.new_y
         print("New coordinates:")
         return (self.new_x, self.new_y)
x = float(input("Print the coordinates of x: "))
y = float(input("Print the coordinates of y: "))

x2 = float(input("Print the coordinates of x of the second point: "))
y2 = float(input("Print the coordinates of y of the second point: "))

new_x = float(input("Print the coordinates of x to move: "))
new_y = float(input("Print the coordinates of y to move: "))
p = Point(x, y)
print(p.show())
print(p.get_dist(x2, y2))
print(p.move(new_x,new_y))


#ex5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposit of", amount, "successful. Balance is now", self.balance)
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal of", amount, "successful. Balance is now", self.balance)
        else:
            print("You don`t have enough money in your balance. Cannot withdraw", amount)

balance = int(input("Enter the initial balance: "))
owner = input("Enter the owner's name: ")

while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        amount = int(input("Enter the amount to deposit: "))
        Account(owner, balance).deposit(amount)
    elif choice == 2:
        amount = int(input("Enter the amount to withdraw: "))
        Account(owner, balance).withdraw(amount)
    elif choice == 3:
        break
#ex6

class Filter:
    def __init__(self, num):
        self.num = num
    
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def prime(self):
        return [x for x in self.num if (lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)))(x)]

num = input("Enter numbers separated by space: ").split()
numbers = []
for i in num:
    numbers.append(int(i))

print("Prime numbers:", *Filter(numbers).prime())
