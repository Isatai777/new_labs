#ex1
# import math
# degree = int(input())
# rad = math.radians(degree)
# print(rad)


#ex2
# height = int(input("height:"))
# base_first_value = int(input("base_first_value:"))
# base_second_value = int(input("base_second_value:"))
# def area_trap(height , base_first_value , base_second_value):
#     square = ((base_first_value + base_second_value) / 2) * height
#     return square
# otvet = area_trap(height , base_first_value , base_second_value)
# print("Expected output:" , otvet)


#ex3
# from math import tan , pi
# n = int(input("Numbers of sides:"))
# l = int(input("Lenght of sides:"))
# s= n*(l** 2)/(4*tan(pi/n))
# print("The area of the polygon is:" , int(s))


#ex4
a = int(input("lenght of base:"))
b = int(input("height of parallelogram: "))
def square_par(a ,b):
    square = a * b 
    return square
otvet = square_par(a,b)
print("Expected Output:" , otvet)
