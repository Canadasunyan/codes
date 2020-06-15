# 平方根取整问题
# 输入一个整数, 返回其平方根的整数部分
# 复杂度log(n)
def calculateSqrt(num):
    low = 0
    high = num
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    while low < high:
        mid = (high - low) // 2 + low
        # [0, 1, 2, 3, 4] | 5, 6, 7, 8, 9
        if mid * mid > num:
            high = mid
        # 0, 1, 2, 3, 4 | [5, 6, 7, 8, 9]
        elif mid * mid < num:
            low = mid + 1
        else:
            return mid
    return high - 1

print(calculateSqrt(25))
