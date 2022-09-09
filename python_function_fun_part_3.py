# name_args - Accepts any number of named arguments and prints them in the pattern key : value one at a time.
def name_args(**kwargs):
    for key in kwargs:
        print(key + " : " + kwargs[key])
# all_true - Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.
def all_true(*input):
    is_true = True
    for item in input:
        if item == False:
            is_true = False
    return is_true

# one_true - Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.
def one_true(*input):
    is_true = False
    for item in input:
        if item == True:
            is_true = True
    return is_true

# recursive_factorial - Uses recursion to find the factorial of an integer.
def recursive_factorial(int):
    if int <= 1:
        return 1
    else:
        return (int * recursive_factorial(int - 1))

# recursive_deduplicate - Recursively removes all adjacent duplicate letters from a string.
# Input: AABBCCDD
# Output: ABCD
def recursive_deduplicate(string, iteration=0):
    if len(string) == 0:
        return "Nothing here!"
    elif len(string) == 1:
        return string
    elif iteration == (len(string) - 1):
        return string
    else:
        if string[iteration] == string[iteration+1]:
            return recursive_deduplicate(string[0 : iteration] + string[iteration + 1 : len(string)], iteration)
        else:
            return recursive_deduplicate(string, iteration + 1)

# recursive_reverse - Uses recursion to reverse a string.
def recursive_reverse(string):
    if len(string) <= 0:
        return
    else:
        return string[-1] + recursive_reverse(string[:-1])

name_args(one = "1", two = "2", three = "3")

print(all_true(True, True, True))
print(all_true(True, True, False))

print(one_true(False, False, False))
print(one_true(True, False, False))

print(recursive_factorial(4)) #4*3*2*1=24 

print(recursive_deduplicate("AAABBBBBCCCCCD"))

string = "testing"
print(string[-1])
print(string[:-1])

print(recursive_reverse("test"))


