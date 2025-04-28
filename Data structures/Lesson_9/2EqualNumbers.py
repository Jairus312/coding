def checkIfSame (number1, number2):
    if ((number1 ^ number2)):
        print("Number are not equal")

    else:
        print("Both numbers are equal.")


number1 = int(input("Enter Number 1 :"))
number2 = int(input("Enter Number 2 :"))

checkIfSame (number1, number2)