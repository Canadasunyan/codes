# 股票利润最大问题
# 输入股票价格, 返回最大利润差, 最大利润差小于0则返回0
def maxProfit(price):
    '''
    price: List[float]
    rtype: float
    '''
    length = len(price)
    # 设置数组记录截至i时刻的历史最低价格
    lowest_price = price[0]
    # 设置数组记录截至i时刻的历史最大利润
    max_profit = 0
    for i in range(1, length):
        if price[i] < lowest_price[i - 1]:
            lowest_price = price[i]
        else:
            lowest_price[i] = lowest_price[i - 1]
        max_profit[i] = max(max_profit[i-1], price[i]-lowest_price[i])
    # print(lowest_price)
    # print(max_profit)
    return max_profit[-1]

if __name__ == "__main__":
    price = [7, 5, 4, 3, 2, 1]
    profit = maxProfit(price)
    print('Max profit: ', profit)