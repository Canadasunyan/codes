# 老鼠走迷宫
# 可行路径由X表示，0代表空地，8代表障碍
# 起点(1, 1), 终点(7, 7)
# 思路：递归法
maze = [[8, 8, 8, 8, 8, 8, 8, 8, 8],
        [8, 0, 0, 0, 0, 0, 0, 0, 8],
        [8, 0, 8, 8, 0, 8, 8, 0, 8],
        [8, 0, 8, 0, 0, 8, 0, 0, 8],
        [2, 0, 2, 0, 2, 0, 2, 0, 8],
        [2, 0, 0, 0, 0, 0, 2, 0, 8],
        [2, 2, 0, 2, 2, 0, 2, 2, 8],
        [2, 0, 0, 0, 0, 0, 0, 0, 8],
        [2, 2, 2, 2, 2, 2, 2, 2, 8]]
# 设置全局变量
success = 0
def visit(i, j):
    global maze
    global success
    # 走一步试试看
    # 此时相当于在(i, j)设置路障
    maze[i][j] = 1
    # 如果路径能达到终点则成功
    if i == 7 and j == 7:
        success = 1
    # 四散找路，往右走一步观察是否有路
    if  success == 0 and maze[i][j + 1] == 0:
        # 递归算法，在(i, j + 1)处做路障标记
        visit(i, j + 1)
    if  success == 0 and maze[i + 1][j] == 0:
        visit(i + 1, j)
    if  success == 0 and maze[i][j - 1] == 0:
        visit(i, j - 1)
    if  success == 0 and maze[i - 1][j] == 0:
        visit(i - 1, j)
    # 如果四个方向都试了但还没成功， 则回退一步
    if success == 0:
        maze[i][j] = 0
    return success

visit(1, 1)
for i in maze:
    print(i)