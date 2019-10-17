# -*- coding: utf-8 -*-

# Test basic grammar
print('Hello, Python!')
print("Hello, Python!")
print('Hello, Python!')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')
print('C:\some\name')
# No avoid
print(r'C:\some\name')
print(3 * 'un' + 'ium')
print('Py' 'thon')
# Prevent End of line by adding a '\' at the end of the line.
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Test function and bacis IO
def hello_Python():  # print input string
    ''' print input string'''
    read_str = input("Please input something:")
    print(read_str)
    return 0

#hello_Python()

# Test control flow
def Fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a + b
    return b

# rev = Fibonacci(input())
# print(rev)

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
# The break statement, like in C, breaks out of the innermost enclosing for or while loop.
# Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement.
def test_prime():
    for x in range(2, 10):
        for n in range(2, x):
            if x % n == 0:
                print(x, "is equal to ", n, "*", x // n, "+", x % n )
                break;
        else:
            print(x, "is a prime number")

#test_prime()

def list_operate():
    # list is immutable
    words = ['cat', 'window', 'defenestrate']
    for str in words:
        print(str, len(str), end = ' ')
    print()
    for iter in range(3):
        print(words[iter], end = ' ')
#list_operate()

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key = lambda pairs: pairs[0])
print(pairs)

def foo(a, b, c, *bypass):
    return len(bypass)

def bar(a, b, c, **bypass):
    a = bypass.get("magicnumber")
    if a == 7:
        return True
    else:
        return False


# test code
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")
# Data structures： list , tuple, dictionary, sequences, sets

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1,7)))

print(result)

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5,6]

results = list(zip(my_strings, my_numbers))

print(results)

a = [1, 3, 5, 7, 9, 11]
b = a[-3:7]
print(b)

def reverseNum(InputNum):
    return int(str(InputNum)[::-1])


InputNum = 123
num_string = str(InputNum)
OutputNum = int(num_string[::-1])
print(OutputNum)