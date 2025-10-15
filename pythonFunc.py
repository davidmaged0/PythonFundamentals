# #Creating a Function
# def my_function():
#     print("Hello from my_function!")
# # Call the function
# my_function()
# def add(x, y):
#     return x + y
# print(add(5, 3))

# def R_shift(x, n):
#     return x >> n
# print(R_shift(8, 2))  # Output: 2
def L_shift(x, n):
    return x << n

# def L_shift_(x, n):
#     print(x << n)

res1 = L_shift(8, n=2)
res1+=1
print(res1)  # Output: 32
def greet(name):
    return f"Hello, {name}!"
message = greet("Alice")
print(message)  # Output: Hello, Alice!

def my_function(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(my_function(4, 1, 2, 1))
##
def func(x=2, y=10,/):
    return x + y
print(func())  # Output: 12
res= func(5,5)
print(res)  # Output: 10
##
def seprateLine():
    print('============')
seprateLine()
def func1(*, x=2, y=10):
    return x + y
print(func1())  # Output: 12
res= func1(x=5,y=5) 
print(res)  # Output: 10
##
def func2(x, y=10, /, *, z=5):  
    return x + y + z
print(func2(3))  # Output: 18
print(func2(3, 4))  # Output: 12
print(func2(3, 4, z=6))  # Output: 13

