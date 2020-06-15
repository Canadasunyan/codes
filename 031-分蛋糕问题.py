# 分蛋糕问题
# 给定一个List表示每个人的需求重量, 另一个List表示每个蛋糕的重量, 每人最多得到一个蛋糕, 蛋糕不能切开, 返回满足需求的人数
# 先排序, 设置两个指针依次扫描列表
def allocate(demand, supply):
    # 优先满足需求较小的人
    demand, supply = sorted(demand), sorted(supply)
    i, j, count = 0, 0, 0
    while i< len(demand) and j < len(supply):
        # 满足需求, 则蛋糕被消耗(j++), 一人离开(i++), 满足的人数加1(count++)
        if demand[i] <= supply[j]:
            i += 1
            j += 1
            count += 1
        else:
            # 如果当前的蛋糕不能满足需求, 则显然不能满足更高的需求, 因此扔掉此蛋糕
            j += 1
    return count

print(allocate([1, 2, 3, 4, 5, 6], [3, 3, 3, 4, 5, 5]))



