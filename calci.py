print("Choose the options for the calculations ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
option=input("Enter the option 1 to 5: ")
b=int(option)
if b==1:
    print("Addition of two numbers")
    num_1=int(input("Enter the first number: "))
    num_2=int(input("Enter the second number: "))
    c=num_1+num_2
    print("The sum of two numbers is", c)
if b==2:
    print("Subtraction of two numbers")
    num_1=int(input("Enter the first number: "))
    num_2=int(input("Enter the second number: "))
    c=num_1-num_2
    print("The subraction of two numbers is", c)
if b==3:
    print("Multiplication of two numbers")
    num_1=int(input("Enter the first number: "))
    num_2=int(input("Enter the second number: "))
    c=num_1*num_2
    print("The multiplication of two numbers is", c)
if b==4:
    print("Division of two numbers")
    num_1=int(input("Enter the first number: "))
    num_2=int(input("Enter the second number: "))
    c=num_1/num_2
    print("The division of two numbers is", c)
else:
    print("The number should be only between 1 to 5")
    