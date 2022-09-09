# Write a Python function called max_num()to find the maximum of three numbers.
from audioop import mul
from math import prod
from operator import truediv


def max_num(*number_list):
    max_number = 0
    for current_Number in number_list:
        if current_Number > max_number:
            max_number = current_Number
    return max_number

print(max_num(11,22,33,44,99,55,66,77,88)) #99

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(*number_list):
    product = 1
    for current_number in number_list:
        product *= current_number
    return product

print(mult_list(1,2,3,4,5)) #120

# Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    return string[::-1]

print(rev_string("!sdrawkcab si sihT"))

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(number, min, max):
    is_in_range = False
    if (number <= max) and (number >= min):
        is_in_range = True
    return is_in_range

print(num_within(15, 10, 25)) #True
print(num_within(5, 10, 25)) #False
print(num_within(10, 10, 25)) #True

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
def pascal(n):
    def generate_row(n, *prev_row):
        if n == 2:
            return
        n_2 = [1]
        i = 0
        while i < len(prev_row) :
            if i == (len(prev_row) - 1):
                n_2.append(1)
            else:
                n_2.append(prev_row[i] + prev_row[i+1])
            i += 1
        print(n_2)
        generate_row(n-1, *n_2)
    if n < 1:
        print("no")
        return
    if n >= 1:
            print([1])
    if n >= 2:
            print([1,1])
    if n >= 3:
        generate_row(n, 1,1)

pascal(5)