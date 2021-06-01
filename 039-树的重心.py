# 重心是指树中的一个结点，如果将这个点删除后，剩余各个连通块中点数的最大值最小，那么这个节点被称为树的重心
N = 8
descendant_maxsize = [0] * N
son = [[] for i in range(N)]
index = 0
descendant_number = [0] * N
# a, b为节点编号, a是b父节点
def add(a, b=None):
    global son, father
    if b is not None:
        son[a].append(b)

def descendants(u):
    global descendant_maxsize, descendant_number
    size, sum = 0, 0
    # 叶子节点则返回
    if not son[u]:
        return 1
    for EachSon in son[u]:
        w = descendants(EachSon)
        size = max(size, w)
        sum += w
    descendant_maxsize[u] = size
    descendant_number[u] = sum
    return sum + 1

add(0)
add(0, 1)
add(0, 2)
add(1, 3)
add(1, 4)
add(2, 5)
add(2, 6)
add(2, 7)
min_weight = N
descendants(0)
for i in range(N):
    weight = max(N - descendant_number[i] - 1, descendant_maxsize[i])
    min_weight = min(min_weight, weight)


