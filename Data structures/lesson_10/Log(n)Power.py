def computePower(x,y):
    result = 1

    while(y > 0):
        if(y % 2 == 0):
            x = x * x
            y >>=1

        else:
            result = result * x
            y = y - 1

        return result
    
print("x^y")
    
x = int(input("Enter your Number x :"))
y = int(input("Enter your Number y :"))

print("Total : ",(computePower(x,y)))