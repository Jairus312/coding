#Program to find the max profit you can get from buying and selling stocks. you can given an array with stocks price for seven days, and you can buy and sell any day.

def calculateProfits(arr,arr_size):
    profit = 0
    for i in range(1, arr_size):
        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]

    return profit
prices = [643,143,341,314,421,323,234,123,121,243,213,214]

profit = calculateProfits(prices, len(prices))
print("Max Profit :", profit)