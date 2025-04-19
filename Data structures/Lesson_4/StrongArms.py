number = int(input("enter a Number :-"))
digits = len(str(number))
resultNumber = 0

temp = number
while temp > 0:
    digit = temp % 10
    resultNumber += digit ** digits
    temp //= 10


if  number == resultNumber:
    print(number ,"is a Amrstrong number.")

else:
    print(number ,"is not a Armstrong number.")    