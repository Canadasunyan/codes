# 除数游戏
# A、B两人博弈，A先写一个整数N, 之后每人写一个数字x, 0 < x < N, N % x == 0, 并更新N = N - x
# 另一方写不出数字则获胜
# 递归方法

def can_win(n, vector):
    if n == 1:
        return False
    if n == 2:
        return True
    else:
        is_win = False
        for i in range(1, n):
            # 在所有能整除的的i当中, 只要有一个能够使得对方获胜, 则己方失败
            if n % i == 0:
                is_win = is_win | (not can_win(n - i, vector))
        vector[n] = is_win
        return vector[n]
def divisor_game(n):
    # 初始化一个向量记录各个值是否被计算过, -1代表未计算, 0代表输, 1代表赢
    # 使用局部变量比全局变量快得多
    vector = [-1] * (n + 1)
    if n == 1:
        print('A获胜！')
    else:
        vector[1] = False
        vector[2] = True
        can_win(n, vector)
        if vector[n]:
            print('B获胜！')
        else:
            print('A获胜！')

divisor_game(40)

# 法二: 数学法, n为奇数则A胜, 偶数则B胜