# Please complete the following functions.

# arb_args - Takes in any number of arguments and prints them one at a time.
def arb_args(*args):
    for item in args:
        print(item)

# inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.
def inner_func(int1, int2):
    def add(add1, add2):
        return (add1 + add2)
    def multiply(mult1, mult2):
        return (mult1 * mult2)
    return (add(int1, int2) + multiply(int1, int2))

# lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.
def lunch_lady(name, preference = "Myestery Meat"):
    print("Hi, " + name + ". Your favorite food is " + preference)

# sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product(int1, int2):
    return (int1 + int2), (int1 * int2)

# alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
# def alias_arb_args(*args):
#     return arb_args(*args)
alias_arb_args = arb_args

# arb_mean - Accepts any number of integers and prints their average.
def arb_mean(*ints):
    def total(*ints):
        total = 0
        for int in ints:
            total += int
        return total
    return (total(*ints)/len(ints))
    

# arb_longest_string - Accepts any number of strings and returns the longest one.
def arb_longest_string(*strings):
    longest_string = ""
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string

test_name = "Euri"
test_string = ["Hello! ","My ","Name ","Is ", test_name]

arb_args("Hello! ","My ","Name ","Is ", test_name)
print(inner_func(2, 5))
lunch_lady("Herv", "Salad")
lunch_lady("Carv")
print(sum_n_product(3, 7))
alias_arb_args("Hello! ","My ","Name ","Is ", test_name)
print(arb_mean(1,2,3,4,5))
print(arb_longest_string("Hello! ","My ","Name ","Is ", test_name))