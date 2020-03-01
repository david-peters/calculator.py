import math

def add (x, y):
    return x + y

def subtract (x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
def subtract(x, y):
   return x - y
def power(x, y):
    return x ** y
def multiplyPower (x, y, z):
    return x ** y * z
def dividePower (x, y, z):
    return x ** y / z
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.power of")
print("6. multiplaying number to power")
print("7. dividing a number to power")



# Take input from the user
choice = input("Enter choice(1/2/3/4/5/6/7): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
elif choice == '5':
    print(num1, "**",num2, "=", power(num1,num2))
elif choice == '6':
    num3 = float(input("Enter third number for multiplying it to the power"))
    print(num1,"**",num2, "*", num3, "=", multiplyPower(num1, num2, num3))
elif choice == '7':
    num3 = float(input("Enter third number for multiplying it to the power"))
    print(num1,"**",num2, "*", num3, "=", dividePower(num1, num2, num3))


else:
   print("Invalid input")