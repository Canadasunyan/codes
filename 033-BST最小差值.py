# BST最小差值
# 给定一个二叉搜索树, 返回其任意两个节点差的绝对值的最小值
# 递归法
import sys
sys.path.append("E:/code/packages")
from BinarySearchTree import *
def minDiff(node):
    # minDiff(r) = min{minDiff(r.left), minDiff(r.right), r - max(r.left), min(r.right - r}
    # 根据节点是否有左右子节点分情况讨论
    # 如果节点为空, 返回无穷大
    if not node:
        return float("inf")
    # 如果node为叶节点, 返回无穷大
    if not node.left and not node.right:
        return float("inf")
    # 初始化左子树最大值和右子树最小值
    l_value, r_value = -float("inf"), float("inf")
    if node.left:
        l = node.left
        # 求max(r.left)
        while l.right:
            l = l.right
        l_value = l.value
    if node.right:
        r = node.right
        while r.left:
            r = r.left
        r_value = r.value
    return min(minDiff(node.left), minDiff(node.right), node.value-l_value, r_value-node.value)

if __name__ == "__main__":
    tree = BinarySearchTree([208,1,-4,13,25,6])
    root = tree.root
    print(minDiff(root))



