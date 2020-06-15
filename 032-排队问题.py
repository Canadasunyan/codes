# 排队问题
# 给定List, 记录每一个人的[身高, 左面比他高的人数), 返回排序后的List, 不存在排列则返回False
# 桶排序法, 先确认最高的人的排列顺序, 再将其他人按顺序插入队列
def requeue(ls):
    """
    type(ls): List[List[int, int]]
    rtype: List[List[int, int]]
    """
    # 先将所有人从高到矮排序
    ls = sorted(ls, key=lambda x: [x[0], -x[1]], reverse=True)
    # 建立新列表, 依次序插入
    new_queue = []
    for i in ls:
        # list.insert(item, place)
        new_queue.insert(i[1], i)
    return new_queue

print(requeue([[1,0], [2, 1], [2, 0], [2, 4], [3, 0], [4, 1], [4, 0]]))


