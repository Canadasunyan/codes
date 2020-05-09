# 二叉搜索树
# 给定一个列表, 返回一个二叉搜索树
#
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.diff = 0

class BinaryTree:
    def __init__(self, values):
        self.root = TreeNode(values[0])
        for value in values[1:]:
            self.insert(self.root, value)
        self.isBalance = self.isBalance(self.root)

    def insert(self, root, value):
        if not root:
            return TreeNode(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        # 更新根节点高度, 由于左右节点可能为None, 不能直接调用self.height
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        root.diff = self.getHeight(root.left) - self.getHeight(root.right)
        balance = self.getHeight(root.left) - self.getHeight(root.right)
        # Step 4 - If the node is unbalanced,
        # 递归函数必须要return
        return root

    def isBalance(self, root):
        if root is None:
            return True
        if root.diff < -1 or root.diff > 1:
            return False
        else:
            return self.isBalance(root.left) and self.isBalance(root.right)

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

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
    a = BinaryTree([2,1,4,3,5,6])
    print(OrderTraversal(a.root))
    print(a.isBalance)