#ex1
# import math
# length = int(input(""))
# numbers = []
# for i in range(length):
#     num = float(input(f"Enter number {i+1}: "))
#     numbers.append(num)
# result = math.prod(numbers)

# print(result)




#ex2
def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
    print(f"Number of lowercase characters: {lower_count}")
    print(f"Number of uppercase characters: {upper_count}")

input_string = input("Enter any string: ")
count_upper_lower(input_string)

#ex3
def is_palindrome(s):
    return s == s[::-1]

user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



#ex4
from time import sleep
import math

def delay(fn, ms, *args):
    sleep(ms / 1000)
    return fn(*args)

def main():
    try:
        user_input_number = float(input("Enter a positive number: "))
        user_input_time = float(input("Enter the delay time in milliseconds: "))

        if user_input_number < 0 or user_input_time < 0:
            print("Please enter positive values for both number and time.")
            return

        result = delay(lambda x: math.sqrt(x), user_input_time, user_input_number)
        print(f"Square root of {user_input_number} after {user_input_time} milliseconds is {result:.15f}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()


#ex5
def all_true(my_tuple):
    return all(my_tuple)

# Example usage
tuple1 = (True, True, True)
tuple2 = (True, False, True)
tuple3 = (False, False, False)

print(all_true(tuple1))  # Output: True
print(all_true(tuple2))  # Output: False
print(all_true(tuple3))  # Output: False




