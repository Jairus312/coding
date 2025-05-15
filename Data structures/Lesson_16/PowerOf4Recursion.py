n = int(input("Enter your number : "))
def checkifPower(n):
    if(n <= 0):
        return False
    if(n == 1):
        return True
    if(n % 4 == 0):
        return checkifPower(n/4)
if (checkifPower(n)):
    print("Power of 4")

else:
    print("Not power of 4")