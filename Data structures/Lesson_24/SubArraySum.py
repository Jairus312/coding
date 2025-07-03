def subarraySum(arr,n,a_sum):
    for i in range(n):
        curr_sum = arr[i]
        j = i + 1
        while j <= n:
            if curr_sum == sum_:
                print("Sum found between")
                print("indexes % d and % d " %(i, j - 1))

                return 1
            if curr_sum > sum_ or j == n:
                break
            curr_sum = curr_sum + arr[j]
            j += 1

    print("No subarray")
    return 0 

arr = [3,6,2,2,56,1,0,9]
n = len(arr)
sum_ = 10
subarraySum(arr, n, sum_)