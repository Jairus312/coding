def tailrec(n, num):
    #Base case: if n exxecds num, terminate the recursion
    if n> num:
        return
    #Print the current value of n
    print(n)
    #recursive call with the next
    tailrec(n + 1, num)
n = int(input("Enter n to print 1 to n : "))
tailrec(1,n)