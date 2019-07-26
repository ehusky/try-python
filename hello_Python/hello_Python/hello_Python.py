# -*- coding: utf-8 -*-

# Test basic grammar
print('Hello, Python!')
print("Hello, Python!")
print('Hello, Python')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')
print('C:\some\name')
print(r'C:\some\name')
print(3 * 'un' + 'ium')
print('Py' 'thon')
# prevent End of line by adding a '\' at the end of the line.
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Test function and bacis IO
def hello_Python():  # print input string
    ''' print input string'''
    read_str = input()
    print(read_str)
    return 0


# 
def Fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b
    return b

rev = Fibonacci(input())
print(rev)