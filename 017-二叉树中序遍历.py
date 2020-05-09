# 二叉树的中序遍历
# 对于二叉搜索树其值为由小到大排列
import sys
sys.path.append("E:/code")
from BinaryTree import *

def inorder(root):
    # 使用栈记录搜索路标
    stack = []
    cur = root
    # 记录输出节点顺序
    nodes = []
    while len(stack) > 0 or cur:
        # 一直搜索左孩子
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            # 搜索到尽头后输出节点
            cur = stack.pop()
            nodes.append(cur)
            right = cur.right
            # 清空输出的节点, 也可以不删
            cur.left = None
            cur.right = None
            cur = right
    return nodes

if __name__ =="__main__":
    a = BinaryTree([1, 3, 2, 5, 4, 6])
    nodes = inorder(a.root)
    print([each.value for each in nodes])