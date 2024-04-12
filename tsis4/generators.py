# #ex1
n = int(input())
for i in range(n):
    squares = (i+1)**2
    print(squares , sep = "\n")


#ex2

def even(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num
n = int(input())
even_numbers = even(n)
print(*even_numbers, sep=", ")


#ex3

def gen_three_for(n):
    for num in range(n+1):
        if num % 3 ==0 and num % 4 == 0:
            yield num


n = int(input())
out_num = gen_three_for(n)
print(*out_num)



#ex4

a = int(input("nachalo intervala:"))
b = int(input("kone4 intervala:"))
def square(a,b):
    for i in range(a , b+1):
        yield i**2
get_num = square(a,b)
print(*get_num)        



#ex5

l1 = []
def back(n):
    while n >=0:
        yield n
        n-= 1 

n = int(input())
get_numbers = back(n)
print(*get_numbers)