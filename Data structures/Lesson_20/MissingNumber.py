def missing_no(arr):
    n = len(arr)
    total = (n + 1) * (n + 2) / 2
    sum_of_arr = sum(arr)
    return total - sum_of_arr


# Driver CODE
arr = [2, 3, 4]
print("The Missing Number IS", missing_no(arr))
