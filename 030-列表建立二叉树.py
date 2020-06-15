# 给定一个List, 按顺序逐行建立二叉树, 余下的部分设为None
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def BinaryTree(ls, root=None, i=0):###用列表递归创建二叉树，
#它其实创建过程也是从根开始a开始，创左子树b，再创b的左子树，如果b的左子树为空，返回none。
#再接着创建b的右子树，
    if i<len(ls):
        if not ls[i]:
            # 如果某一数值为None, 则其左右子节点即使存在数值也会被清除
            return None
        else:
            # [1, 2, 3, 4, 5, 6], i = 0
            root=TreeNode(ls[i])
            # 1的左孩子是2, 右孩子是3
            # 2的左孩子是4, 右孩子是5, 以此类推
            # 从根开始一直到最左, 直至为空
            root.left=BinaryTree(ls, root.left, 2 * i + 1)
            # 再返回上一个根, 回溯右
            root.right=BinaryTree(ls, root.right, 2 * i + 2)
            # 建立子树完毕, 返回其根节点
            return root  ###这里的return很重要
    # 列表最后一部分数字为叶节点, 直接返回其数值
    # 假设层数为n, 节点数为m, 则共有m + 1 + m % 2 - 2^(n-1) 个叶子节点, 满足2 * i + 1 >= len(ls)
    return root
llist=[1, None, 3, 4, 5]
root = BinaryTree(llist)

