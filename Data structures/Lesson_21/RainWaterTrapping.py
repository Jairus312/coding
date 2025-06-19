def findwater(a, a_size):
    leftTallest = [0]*a_size
    rightTallest = [0]*a_size
    water = 0
    leftTallest[0] = a[0]
    for i in range(1, a_size):
        leftTallest[i] = max(leftTallestTallest[i-1],a[i])

    rightTallest[0] = a[0]
    for i in range(1, a_size):
        rightTallest[i] = max(rightTallest[i+1],a[i])
            
    for i in range(0, a_size)  