# 求二叉树中所有节点与其祖先节点差的绝对值的最大值
# 初始化两个类：节点类和二叉树类
# 也可以import binarytree
class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value  # 节点的值
        self.left = left  # 左子节点
        self.right = right  # 右子节点

class BinaryTree:
    def __init__(self, seq=()):
        # assert isinstance(seq, Iterable)  # 确保输入的参数为可迭代对象
        self.root = None
        # 给二叉树赋值
        self.insert(*seq)

    def insert(self,*args):
        # 输入为空则直接返回
        if not args:
            return
        self.root = Node(args[0])
        args = args[1:]
        # 从第一个子节点开始发展
        for i in args:
            # 每插入一个节点, 都要从根节点开始插入
            seed = self.root
            while True:
                if i > seed.value:
                    if not seed.right:
                        node = Node(i)
                        seed.right = node
                        break
                    else:
                        seed = seed.right
                else:
                    if not seed.left:
                        node = Node(i)
                        seed.left = node
                        break
                    else:
                        seed = seed.left

def MaxDiff(root_node, l, r):
    # l, r记录该节点路径上的最大值和最小值
    if not root_node:
        return 0
    # 游标记录当下的节点与其祖先节点的差的最大绝对值
    cur = max(abs(root_node.value - l),abs(root_node.value - r))
    # 最大绝对值出现在三种情况, 当下节点，当下节点的右孩子或左孩子
    # 对于左右孩子, 加入了一个节点之后, 该路径上的最大值或最小值可能发生变化
    l = min(l,root_node.value)
    r = max(r,root_node.value)
    return max(cur,MaxDiff(root_node.left,l,r),MaxDiff(root_node.right,l,r))

bt = BinaryTree([8, 3, 10, 1, 6, 14, 4, 7, 13])
root_node = bt.root
# 根节点的路径只有一个元素, 因此最大值和最小值相等
val = MaxDiff(root_node, root_node.value, root_node.value)
print('该二叉树最大绝对值差: ', val)

