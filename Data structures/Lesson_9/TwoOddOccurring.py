def printTwoOdd(arr, size):
    x = 0
    y = 0

    Setbit = 0
    for i in range(1, size):
        xorof2 = xorof2 ^ arr[i]

    Setbit = xorof2 & ~(xorof2 - 1)

    for i in range(size):
        if(arr[i] & Setbit):
            x = x ^ arr[i]

        else:
            y = y ^ arr[i]

print("The two Odd element are", x,"&",y)
arr_size = int(input("enter size of array :"))
for i in range(0,arr_size):
     z = int(input("Enter Element :"))
     arr.append(z)
printTwoOdd(arr,arr_size)