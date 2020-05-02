# 合并两个从小到大排序的列表
# 使用链表结构
class LinkNode:
    def __init__(self, n):
        self.value = n
        self.next = None

# 打印一个链表
def PrintLinkList(head):
    ls = []
    while True:
        if not head:
            return ls
        else:
            ls.append(head.value)
            head = head.next

# 建立链表
def MergeSortedList(ls1 = [1, 2, 3, 4, 5], ls2 = [1, 3, 5, 7, 9]):
    # 建立头指针
    cur = l1 = LinkNode(0)
    for each in ls1:
        cur.next = LinkNode(each)
        cur = cur.next
    # 去掉头指针
    l1 = l1.next
    cur = l2 = LinkNode(0)
    for each in ls2:
        cur.next = LinkNode(each)
        cur = cur.next
    l2 = l2.next
    cur = head = LinkNode(0)
    while l1 and l2:
        if l1.value < l2.value:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    # 剩余的数据粘在最后面
    cur.next = l1 or l2
    return PrintLinkList(head.next)


