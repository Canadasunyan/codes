# 二叉平衡树
# 给定一个列表, 返回一个二叉平衡树
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self, values):
        # 先初始其根节点
        self.root = None
        for value in values:
            # 每插入一个数根节点就可能更新一次
            self.root = self.insert(self.root, value)

    def insert(self, root, value):
        # 递归
        if not root:
            return TreeNode(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        # 更新根节点高度, 由于左右节点可能为None, 不能直接调用self.height
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)
        # 添加一个数后AVL树不平衡, 则旋转子树, 分四种情况
        #         root
        #       /      \
        #      l        r
        #    /   \    /   \
        #   a     b  c     d
        # case 1 - l > r, and a > b (left left)
        if balance > 1 and value < root.left.value:
            # 旋转子树, 改变根节点
            return self.rightRotate(root)
        # Case 2 - l < r, and c < d (right right)
        if balance < -1 and value > root.right.value:
            return self.leftRotate(root)
        # 以上两种情况只需要旋转一次, 下面两种情况需要旋转两次
        # Case 3 - l > r, and a < b (left right)
        if balance > 1 and value > root.left.value:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # Case 4 - l < r, and c > d (right left)
        if balance < -1 and value < root.right.value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
            # 递归函数必须要return
        return root

    def leftRotate(self, root):
        r = root.right
        c = r.left
        # Perform rotation
        r.left = root
        root.right = c
        # Update heights
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        r.height = 1 + max(self.getHeight(r.left), self.getHeight(r.right))
        # Return the new root
        return r

    def rightRotate(self, root):
        l = root.left
        b = l.right
        # Perform rotation
        l.right = root
        root.left = b
        # Update heights
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        l.height = 1 + max(self.getHeight(l.left), self.getHeight(l.right))
        # Return the new root
        return l

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

def orderTraversal(a):
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
    a = AVLTree([2, 1, 4, 3, 5, 6])
    print(orderTraversal(a.root))