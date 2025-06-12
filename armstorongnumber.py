def armstrong_number(number):
    num=str(number)
    num_digits=len(num)
    sum_of_all=sum(int(digit)**num_digits for digit in num)
    return sum_of_all==number

number=int(input("Enter the number: "))
if armstrong_number(number):
    print(number,"is an Armstrong number")
else:
    print(number,"is not an Armstrong number")