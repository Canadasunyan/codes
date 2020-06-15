# 求和近似问题
# 给定一个序列, 输出其中任意三个数之和, 使其尽可能接近目标值
def closestSum(ls, target):
    """
    type(ls): List[int]
    type(target): int
    rtype: int
    """
    # 先对列表快排
    ls = sorted(ls)
    # 初始指针指向0, 1, -1
    result = ls[0] + ls[1] + ls[len(ls)-1]
    for i in range(len(ls)-2):
        # 对于每一个值, 在其右侧区间选择两个数, 并进行比较, 从两端算起
        l = i + 1
        r = len(ls) - 1
        while l < r:
            value = ls[i] + ls[l] + ls[r]
            if value == target:
                return target
            elif value <= target:
                l += 1
            else:
                r -= 1
            if abs(value-target) < abs(result-target):
                result = value
    return result



