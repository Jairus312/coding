def MaxElementArray(a):
    length = len(a)
    if length == 1:
        return a[0]
    return max(a[0],MaxElementArray(a[1:]))
a = [1,10,100,1000,10000000000000000000000]
print("Largest Element of array : ", MaxElementArray(a))