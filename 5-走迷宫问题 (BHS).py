# 老鼠走迷宫(2)
# 可行路径由X表示，0代表空地，8代表障碍
# 起点(1, 1), 终点(7, 7)
# 思路：广度优先搜索 (BFS)
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
    # 建立一个空队列存储所有访问的节点
    queue = []
    if maze[i][j] == 2:
        print('No feasible route!')
    else:
        queue.append([i, j])
    # 建立字典储存其上一个节点
    dict = {}
    while queue:
        if [7, 7] in queue:
            success = 1
            break
        xi, xj = queue.pop()
        maze[xi][xj] = -1
        if maze[xi][xj + 1] == 0:
            queue.append([xi, xj + 1])
            dict[str([xi, xj + 1])] = [xi, xj]
        if maze[xi][xj - 1] == 0:
            queue.append([xi, xj - 1])
            dict[str([xi, xj - 1])] = [xi,xj]
        if maze[xi + 1][xj] == 0:
            queue.append([xi + 1, xj])
            dict[str([xi + 1, xj])] = [xi,xj]
        if maze[xi - 1][xj] == 0:
            queue.append([xi - 1, xj])
            dict[str([xi - 1, xj])] = [xi,xj]
    if success == 1:
        return dict
    else:
        print('No feasible route!')

dict = visit(1, 1)
if dict:
    route = [[7, 7]]
    father_node = dict['[7, 7]']
    while father_node != [1, 1]:
        route.append(father_node)
        father_node = dict[str(father_node)]
    route.append([1, 1])
    route.reverse()
    print(route)

