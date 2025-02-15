'''
This code demonstrates the use of logical operators in Python.
'''
a = 10
b = 20
c = 30
e = 40
f = 50
g = 60
h = 70
i = 80
j = 90
k = 100

# and operator
if a > b and a > c:
    print("a is the largest number")
elif b > a and b > c:
    print("b is the largest number")
else:
    print("c is the largest number")
# or operator
if a > b or a > c:
    print("a is the largest number")
elif b > a or b > c:
    print("b is the largest number")
else:
    print("c is the largest number")
# not operator
if not a > b:
    print("a is not greater than b")
else:
    print("a is greater than b")
if a > e and e > f:
    print("a is the largest number.")
elif e > a and e > f:
    print("f is the largest number")
if a > e or a > e:
    print("a is the largest number")
elif not a > e:
    print("a is not grater than e")
if a > f and f > g:
    print("g is the largest number")
