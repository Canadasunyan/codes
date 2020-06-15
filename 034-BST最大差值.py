# BST最大差值
# 给定一个二叉搜索树, 返回其任意两个节点差的绝对值的最小值
# 递归法
import sys
sys.path.append("E:/code/packages")
from BinarySearchTree import *

def maxDiff(root):
    # 设置两个节点指向最大值和最小值
    l, r = root, root
    while l.left:
        l = l.left
    while r.right:
        r = r.right
    return r.value - l.value

    

if __name__ == "__main__":
    tree = BinarySearchTree([208,1,-4,13,25,6])
    root = tree.root
    print(maxDiff(root))



