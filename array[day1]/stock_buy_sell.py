def stock(arr):
    day_buy = 0
    day_sell = 1
    profit = 0
    while day_sell < len(arr):
        if arr[day_sell] > arr[day_buy]:
            today_profit = arr[day_sell] - arr[day_buy]
            profit = max(profit,today_profit)
        else:
            day_buy = day_sell
        day_sell = day_sell+1
    return profit

print(stock([7,6,4,3,1]))