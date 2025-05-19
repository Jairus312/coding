def ways(Stairs):
    # Check corner case
    if Stairs < 0:
        return 0
    # if no Stairs left, just return one as  we reach  the top 
    if Stairs == 0:
        return 1
    TwoSteps = 0
    OneStep = 0
    # We can jump 2 steps
    if(Stairs >= 2):
        TwoSteps = ways(Stairs - 2)
    # Jump 1 if 1 or more Stairs remains
    OneStep = ways(Stairs - 1)
    # return total ways
    return TwoSteps + OneStep
Stairs = int(input("Enter number of steps : "))
print("Number of ways to climb : ", ways(Stairs))