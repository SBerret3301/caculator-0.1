x = float(input(" enter the first number :" ))
y = float(input(" enter the second number :" ))
print("num1 + num2 = :", x + y)
print("num1 - num2 = :", x - y)
print("num1 x num2 = :", x * y)
while y == 0 :
    y = float(input("type a defferent number : "))
while y != 0 :
    print("the real quotient is :", x / y )
    print("the entire quotient is :", x//y)
    print("the rest of the division is :", x%y)
    break
print("the average of two numbers is :", (x+y)/2)