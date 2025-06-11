num=int(input("Enter the Number: "))
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
class Book():
    def oddoreven():
        if num % 2 == 0:
            return "Even"
        else:
            return "Odd"
    def prime():
        sq=num**0.5
        c=int(sq+1)

        for i in range (2,c+1):
            if num%i==0:
                return "not prime number"
            else:
                return "prime number"
    def aplusb():
        g=a**2
        h=b**2
        i=2*a*b
        j=g+h+i
        return j
    
class Book2(Book):
    def sample1():
         g=a**2
         h=b**2
         i=2*a*b
         j=g+h+i
         return j


k=Book.aplusb()
print(k)
x=Book.oddoreven()
print(x)
y=Book.prime()
print(y)
