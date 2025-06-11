num=int(input("Enter the Number: "))
def oddoreven(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
x=oddoreven(num)
print(x)

def prime(num):
    sq=num**0.5
    c=int(sq+1)

    for i in range (2,c+1):
        if num%i==0:
            return "not prime number"
        else:
            return "prime number"
y=prime(num)
print(y)