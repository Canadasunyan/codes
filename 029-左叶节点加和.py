# 左子树加和
# 给定一个二叉树, 返回所有左叶子的和
# 带标签的递归, 设置标签side标示搜寻的是左子树还是右子树
import sys
sys.path.append("E:/code/packages")
from AVLTree import *

def sumLeftLeaves(root, side=''):
    if not root:
        return 0
    # 如果不是叶子节点, 则返回两子树的和
    elif root.left or root.right:
        return sumLeftLeaves(root.left,'l') + sumLeftLeaves(root.right, 'r')
    # 如果是叶子节点, 则仅在其为左节点时加和
    elif side == 'l':
        return root.value
    # 右节点则加0
    else:
        return 0
if __name__ == "__main__":
    tree = AVLTree([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(sumLeftLeaves(tree.root))
