# 二叉树的层序遍历
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value  # 节点的值
        self.left = left  # 左子节点
        self.right = right  # 右子节点

def OrderTraversal(a):
    '''
    a: BinaryTree
    rtype: list[list[int]]
    '''
    # a不为空则先加入根节点
    if a:
        # ls存储每一层的数值
        ls = [[a.value]]
    # 为空则返回None
    else:
        return
    # 每一层用一个list记录
    layer = []
    if a.left:
        layer.append(a.left)
    if a.right:
        layer.append(a.right)
    while layer:
        ls.append([each.value for each in layer])
        next_layer = []
        # 注意添加节点的顺序
        for each in layer:
            if each.left:
                next_layer.append(each.left)
            if each.right:
                next_layer.append(each.right)
        # 更新layer
        layer = next_layer
    return ls

if __name__ =="__main__":
    a = BinaryTree(1)
    l = a.left = BinaryTree(2)
    l.right = BinaryTree(4)
    l.left = BinaryTree(5)
    r = a.right = BinaryTree(2)
    r.left = BinaryTree(4)
    rr = r.right = BinaryTree(5)
    rr.right = BinaryTree(6)
    print(OrderTraversal(a))
