# 列表中位数问题
# 给定两个从小到大排序好的列表, 返回这两个列表的中位数, 要求时间复杂度O(log(n))
# 分情况讨论
import numpy as np
def median(a, b):
    la, lb, mid = len(a), len(b), (len(a) + len(b)) // 2
    # A = [a1, a2, a3, ..., am], B = [b1, b2, b3, ..., bn]
    # 保证m始终不小于n
    if la < lb:
        a, b = b, a
    # 情况1, am < b0, 则中位数可以立即确定, 复杂度O(1)
    if a[-1] < b[0]:
        if la == lb:
            return (a[-1] + b[0]) / 2
            # 中位数必在a中产生, 个数为奇数则返回中间值, 偶数则返回中间两个的平均值
        else:
            return a[mid] if (la + lb) % 2 else (a[mid] + a[mid - 1]) / 2
    # 情况2, a0 > bn, 则中位数可以立即确定, 复杂度O(1)
    if b[-1] < a[0]:
        if la == lb:
            return (b[-1] + a[0]) / 2
        else:
            return a[(la - lb) // 2] if (la + lb) % 2 else (a[(la - lb) // 2] + a[(la - lb) // 2 - 1]) / 2
    # 其他情况, 需要求出所有元素中排在中间位置的一个(或两个)数
    # eg: a[9] = [2, 4, 6, 8, 10, 12, 14, 16, 17], 9
    #                   p  p+1
    #     b[6] = [-1, 1, 3, 5, (7), 9], 则中位数由
    #                           q  q+1
    # a[p], a[p + 1], b[q], b[q + 1]四个数决定, 使用二分搜索找出p, q的值, 使得:
    # p + q = (a + b) / 2, 且小于等于a[p]或b[q]的数恰有(a+b)//2个, 即
    # a[p] >= b[q], 且a[p] < b[q + 1], 或b[q] >= a[p], 且b[q] < a[p + 1]
    # p初始化为la // 2 - 1, q = lb // 2 - 1
    ###注意### 防止q超出list标号
    # 中位数肯定位于a的范围内, 但不一定是a中的数
    p = (la - 1) // 2
    q = mid - p - 1
    lcur, rcur = 0, lb - 1
    # a[p], b[q]两个数之前的数字总有mid - 1个
    # 循环直到小于等于a[p], b[q]其中一个数的数字恰有mid - 1个
    # 二分搜索查找合适的q, 保证p, q不能越界
    while lcur < rcur:
        print('p: ', p, 'q: ', q)
        val1, val2 = a[p], b[q]
        if val1 < val2:
            rcur = q
            q = (q + lcur) // 2
            p = mid - q - 1
        elif val1 > val2:
            lcur = q
            q = (q + rcur) // 2
            p = mid - q - 1
        # 若a[p] = b[q], 则直接得到中位数
        else:
            return val1
        print(p, q, lcur, rcur)
    # q如果超出标号, 则说明q里的元素都很小, 直接返回p中某元素
    if (la + lb) % 2:
        print(q)
        if a[p] < b[q]:
            return min(a[p + 1], b[q])
        # q没超出编号, 则进行比较
        elif q < lb - 1:
            return min(a[p], b[q + 1])
        # 否则直接输出a[p]
        else:
            return a[p]
    else:
        if q < lb - 1:
            return (min(a[p + 1], b[q]) + a[p]) / 2 if a[p] <= b[q] else (min(a[p], b[q + 1]) + b[q]) / 2
        else:
            return (min(a[p + 1], b[q]) + a[p]) / 2 if a[p] <= b[q] else (a[p] + b[q]) / 2

a = [1, 3, 5, 7, 9, 9, 11, 12, 13, 14, 19]
b = [16, 17]
predict_val = median(a, b)
true_val = np.median(a + b)
print('len=', len(a)+len(b), ', predict = ', predict_val, ', true = ', true_val, predict_val == true_val)







