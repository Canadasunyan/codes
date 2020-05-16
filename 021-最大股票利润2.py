# 股票利润最大问题 (2)
# 输入股票价格, 返回:
# 1. 最大利润差, 最大利润差小于0则返回0, 允许多次交易
# 2. 交易记录, -1表示买入, 1表示卖出, 0表示不作处理
def maxProfit(price):
    '''
    price: List[float]
    rtype: float
    '''
    length = len(price)
    # 设置变量记录上一个时间点的价格
    previous_price = price[0]
    # 设置变量记录最大利润
    max_profit = 0
    action = [0] * length
    for i in range(length):
        if price[i] > previous_price:
            action[i-1] -= 1
            action[i] += 1
            max_profit += price[i] - price[i-1]
        previous_price = price[i]
    # print(lowest_price)
    # print(max_profit)
    return action, max_profit

if __name__ == "__main__":
    price = [1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 5, 1]
    action, profit = maxProfit(price)
    print('Action: ', action)
    print('Max profit: ', profit)