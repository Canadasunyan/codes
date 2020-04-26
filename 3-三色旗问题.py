# 三色旗问题，随机生成红白蓝三色旗，并排列成蓝->白->红的顺序
# 生成随机序列
import numpy as np

def generate_array(n):
    ls = np.random.randint(3,size=n)
    # 列表生成器
    color_list = [None for i in range(n)]
    for each in range(n):
        if ls[each] == 0:
            color_list[each] = '红'
        elif ls[each] == 1:
            color_list[each] = '白'
        else:
            color_list[each] = '蓝'
    return color_list

def swap(ls):
    # 设置三个指针，r, w, b
    # b指针左侧全是蓝色
    # r指针右侧全是红色
    # w指针在两指针之间移动
    b = w = 0
    r = len(ls) - 1
    # 打印原始array
    print('原始序列0：', ls)
    count = 1
    # 开始循环，w指针永远在r指针左侧
    while w <= r:
        if ls[b] == '红' and ls[r] == '蓝':
            # 调换两面旗帜
            ls[b], ls[r] = ls[r], ls[b]
            b += 1
            r -= 1
            w = b
            print('第%d次交换：' % count, ls)
            count += 1
        elif ls[b] == '蓝':
            # b指针右进1
            b += 1
            w += 1
        elif ls[r] == '红':
            # r指针左进1
            r -= 1
        elif ls[w] == '蓝' and ls[b] != '蓝' :
            # 交换旗帜
            ls[b], ls[w] = ls[w], ls[b]
            b += 1
            print('第%d次交换：' % count, ls)
            count += 1
        elif ls[w] == '红' and ls[r] != '红' :
            # 交换旗帜
            ls[r], ls[w] = ls[w], ls[r]
            r -= 1
            print('第%d次交换：' % count, ls)
            count += 1
        elif ls[w] == '白':
            w += 1

ls = generate_array(20)
swap(ls)