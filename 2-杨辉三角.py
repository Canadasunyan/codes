# 杨辉三角
#         1
#     1   2   1
#  1    3   3    1
# 求第i行的第j个数
# 法1：公式法
def get_value(i, j):
    p = 1
    if j == 0:
        return 1
    elif j < i:
        for k in range(1, j + 1):
            p = p * (i - k + 1) / k
        return p
    elif j == n:
        return 1


# 法2：递归法
def get_value(i, j):
    global n
    if j == 0:
        return 1
    elif i == j:
        return 1
    else:
        return get_value(i - 1, j - 1) + get_value(i - 1, j)


# 输入三角形行数
def print_triangle(n):
    for i in range(n):
        # 打印第一行
        if i == 0:
            for each in range(n):
                print('    ', end='')
            print('   1')
        else:
            for j in range(i):
                if j == 0:
                    # 打印空位
                    for each in range(n - i):
                        print('    ', end='')
                    print('%4d' % get_value(i, j), end='')
                else:
                    print('    ', end='')
                    print('%4d' % get_value(i, j), end='')
            print('        1\n')


n = int(input('输入杨辉三角行数！'))
print_triangle(n)
