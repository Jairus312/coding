def max1(number):
    count = 0
    while(number!=0):
        number = (number & (number << 1))

        count = count+1

    return count

number = int(input("Enter your number : "))
print("longest conseccutive 1's are : " ,max1(number))