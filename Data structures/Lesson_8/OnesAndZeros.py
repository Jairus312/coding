#Functions taking our number as input
def numberofbits(n):
    ones = 0
    zeros = 0

#While our number is greater than zero last bit and right shift
    while (n):
    #use AND operator to check if the last bit is 1 or 0
     if(n&1==1):
        ones += 1

     else:
        zeros += 1

     n >>= 1

    print("\n\n Ones = ",ones,"\nZeros",zeros)

number = int(input("Enter your number : "))
numberofbits(number)