#PYTHON FUNCTIONS 1
#ex1
'''
def ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
print(ounces(int(input())))'''
#ex2
'''def c(f):
    c = (5/9)* (f-32)
    return c
print(c(int(input())))'''
#ex3
'''def solve(numheads, numlegs):
    chicken = 0
    rabbit = 0
    rabbit = (numlegs - 2*numheads) /2
    chicken = numheads - rabbit
    print("Number of chickens: ", int(chicken),"\n" "Number of rabbits: ", int(rabbit))

print(solve(35,94))'''
#ex4
'''def prime(ro):
     prime_numbers = []
     for num in ro:
         if is_prime(num):
             prime_numbers.append(num)
     return prime_numbers
def is_prime(num):
     if num <= 1:
         return False
     for i in range(2, num):
         if num % i == 0:
             return False
     return True

ro = input().split(' ')
new = []
for i in ro:
    new.append(int(i))

print(*prime(new))
'''
#ex5
'''import itertools
from itertools import permutations
abc = input().split(" ")
perm = permutations(abc)
for i in list(perm):
    print(i)'''
#ex6
'''re = input().split()
for i in range(len(re)-1, -1,-1):
    print(re[i], end = " ")'''
#ex7
'''def has_33(ra):
    if len(ra) == 3:
        return True
    return False
ra = input().split()
print(has_33(nums))'''
#ex8
'''def spy_game(ru):
    for i in range(0,len(ru)):
        if ru[i] == 0:
            for x in range(i+1,len(ru)):
                if ru[x] == 0:
                    for y in range(x+1,len(ru)):
                        if ru[y] == 7:
                            return True
                    else:
                        return False

ru = input().split()
l = []
for i in ru:
    l.append(int(i))
print(spy_game(l))'''

#ex9
'''import math
def square(radius):
    square = 4/3 * math.pi * radius**3
    return square
print(square(int(input())))'''
#ex10
'''def unique(y_list):
    ri = []
    for i in y_list:
        if i not in ri:
            new.append(i)
    return ri

y_list = input().split()
print(*unique(y_list))'''
#ex11
def palindrome(word):
    for i in range(0, int(len(word)/2)):
        if word[i] != word[len(word)-i-1]:
            return False
    return True

word = input("Give me a word for checking palindrome: ")
print(palindrome(word))
#ex12
def histogram(stars):
    for i in range(len(stars)):
        print(int(stars[i]) * '*')

stars = input("Give me numbers and I will send you a stars ").split()
rus = []
for i in stars:
    rus.append(i)

print(histogram(rus))

#ex13
import random
secret = random.randint(1,20)
print("Hello! What is your name?")
name = input()
print("Well,", name, ", I am thinking of a number between 1 and 20.")
print("Take a guess.")
number = int(input())
iter =0
while (number !=secret):
        if number > secret:
            print("Your guess is too high.")
            print("Take a guess.")
        if number < secret:
            print("Your guess is too low.")
            print("Take a guess.")
        number = int(input())
        iter +=1
if number == secret:
    print("Good job, ",name,"! You guessed my number in ",iter," guesses!")

