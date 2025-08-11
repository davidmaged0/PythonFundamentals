"""my_array = [7, 12, 9, 4, 11]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i

print('Lowest value:',minVal)"""
##The Fibonacci Number Algorithm

x1 ,x2 =0 , 1
print(x1)
print(x2)
for i in range(2, 10):
    x3 = x1 + x2
    print(x3)
    x1 = x2
    x2 = x3