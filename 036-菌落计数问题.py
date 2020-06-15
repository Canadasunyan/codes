# 菌落计数问题
# 给定一个矩阵, 输出矩阵中菌落的数量, 菌落与菌落之间必须间隔1个".", 有菌落的区域用"x"表示
# 按次序扫描每个点, 使用递归将与某区域相连的所有菌落消除, 同时count+=1
def count(mat):
    # 找到一处菌落则将菌落中所有点改标成'.', 使用递归法
    def changeColor(i, j):
        # 递归需要确认参数范围
        while i >= 0 and i < len(mat) and j >= 0 and j < len(mat[0]):
            if mat[i][j] == '.':
                return mat
            else:
                mat[i][j] = '.'
                changeColor(i - 1, j)
                changeColor(i + 1, j)
                changeColor(i, j - 1)
                changeColor(i, j + 1)
                return mat
    # 初始化计数器
    count = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 'x':
                count += 1
                mat = changeColor(i, j)
    return count





if __name__ == "__main__":
    # 该矩阵中有7个菌落
    mat = [['x','.','x','x','.','x','x'],
           ['x','.','x','x','.','.','.'],
           ['x','.','.','.','.','x','x'],
           ['.','.','x','x','.','x','x'],
           ['x','x','.','.','.','.','.'],
           ['x','x','.','x','x','x','x']]
    print(count(mat))
