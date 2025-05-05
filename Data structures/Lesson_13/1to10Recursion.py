#Recursive function that will accept n till we reach 10 
def print1to10(n):
    #Base case to stop recursion
    if(n>10):
        return
    print(n)
    #Recursive call 1 -> 2, 2 -> 3, 3 -> 4 and so on 
    print1to10(n + 1)

print1to10(1)