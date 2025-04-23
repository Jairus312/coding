#Return true if n is even, else odd
def isEvenOdd(n):
    if(n ^ 1):
        return True;
    else:
        return False;

number = int(input("Enter your Number : "))

if isEvenOdd(number):
    print(number,"is Even.")

else:
    print(number,"is Odd.")