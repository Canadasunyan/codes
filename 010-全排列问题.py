# 全排列问题, 输入一个序列, 返回其所有可能的排列
# 递归法
def permute(nums):
    """
    type nums: list[int]
    rtype: list[list[int]]
# 全排列问题, 输入一个序列, 返回其所有可能的排列
# 递归法

def permute(nums, repeat = 0):

    """
    type nums: list[int]
    rtype: list[list[int]]
    """
    if len(nums) <= 1:
        # 必须加方括号, 保证输出的类型永远是list[list[int]]
        return [nums]
    answer = []
    # enumerate函数: 输入list返回序号及值的元组
    for i, i_value in enumerate(nums):
        # 先提取出第i个元素, 放在第一个
        n = nums[:i] + nums[i + 1:]
        # 剩下的元素递归上述操作直至n = 1
        for y in permute(n):
            # python列表操作: 列表 + 列表 = 列表
            item = [i_value] + y
            if repeat:
                if item not in answer:
                    answer.append(item)
            else:
                answer.append(item)
    return answer

ls = [1, 1, 2, 3, 4]
# 判断提到外面去, 递归函数内部越少越好
if len(ls) != len(set(ls)):
    print(permute(ls, repeat=1))
else:
    print(permute(ls))


# 分析: pm([1, 2, 3]) -> pm([2, 3] + 1) -> pm([2] + 3 + 1) -> append(2, 3, 1)
#                                                           -> pm([3] + 2 + 1) -> append(3, 2, 1)
#                              -> pm([1, 3] + 2) -> pm([1] + 3 + 2) -> append(1, 3, 2)
#                                                           -> pm([3] + 1 + 2) -> append(3, 1, 2)
#                              -> pm([1, 2] + 3) -> pm([1] + 2 + 3) -> append(1, 2, 3)
#                                                           -> pm([2] + 1 + 3) -> append(2, 1, 3)