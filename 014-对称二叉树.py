# 给定一个二叉树, 判断其是否对称
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value  # 节点的值
        self.left = left  # 左子节点
        self.right = right  # 右子节点

def isSymmetricTree(left, right):
    '''
    a: BinaryTree
    rtype: Binary
    '''
    # 二者都为空则相同
    if left is None and right is None:
        return True
    # 左右子树恰有一个非空, 则不同
    if left is None or right is None:
        return False
    # 左右子树均不为空, 则比较值和其子树
    else:
        return left.value == right.value and isSymmetricTree(left.right, right.left) and isSymmetricTree(left.left, right.right)

if __name__ =="__main__":
    #             1
    #          /     \
    # a  =    2       3
    #       /   \   /   \
    #      5     4 4     5
    a = BinaryTree(1)
    l = a.left = BinaryTree(2)
    l.right = BinaryTree(4)
    l.left = BinaryTree(5)
    r = a.right = BinaryTree(2)
    r.left = BinaryTree(4)
    r.right = BinaryTree(5)
    print(isSymmetricTree(a.left, a.right))