def MaxElementArray(a):
    length = len(a)
    if length == 1:
        return a[0]
    return max(a[0],MaxElementArray(a[1:]))
a = [1,2345,345,45,456,56,5678,678,78]
print("largest element of array : ",MaxElementArray(a))