# 给定两个二叉树, 判断其是否相同
class BinaryTree:
    def __init__(self,value,left=None,right=None):
        self.value = value  # 节点的值
        self.left = left  # 左子节点
        self.right = right  # 右子节点

def isSameTree(a, b):
    '''
    a: BinaryTree
    b: BinaryTree
    '''
    # a, b均为空则相同
    if a is None and b is None:
        return True
    # 一个为空且另一个不为空则不同
    if a is None or b is None:
        return False
    # 两个均不为空, 则先比较节点的值, 再比较其左右子树是否相同
    else:
        return a.value == b.value and isSameTree(a.left, b.left) and isSameTree(a.right, b.right)

if __name__ =="__main__":
    #        1
    # a =  /   \
    #     2     3
    a = BinaryTree(1)
    a.left = BinaryTree(2)
    a.right = BinaryTree(3)
    b = BinaryTree(1)
    b.left = BinaryTree(2)
    b.right = BinaryTree(3)
    print(isSameTree(a, b))