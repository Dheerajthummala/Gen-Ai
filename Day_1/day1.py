def addition(a,b):
    return a+b
def subraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b  
def division(a,b):
    return a/b   
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
selection = input("select(+,-,*,/): ")
result = 0
if selection == "+":
    result = addition(x, y)
elif selection == "-":
    result = subraction(x, y)
elif selection == "*":
    result = multiplication(x, y)
elif selection == "/":
    result = division(x, y)
print("Result:", result)
