def minElement(a, size):
    temp = a[0]
    for i in range(1,size):
        temp = min(temp,a[i])
        return temp
    
    
def maxElement(a, size):
    temp = a[0]
    for i in range(1,size):
        temp = max(temp,a[i])
        return temp
    
a = [12, 1234, 45 ,74]
size = len(a)
print("Minimum Element of array", minElement(a,size))
print("Maximum Element of array", maxElement(a, size))