# 列表反转
# 设置dummy node, 依次插入元素, 拼接出反转的列表
class LinkNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def linkList(values):
    head = cur = LinkNode(0)
    for each in values:
        node = LinkNode(each)
        cur.next = node
        cur = cur.next
    return head.next

def reverseLink(head):
    # 1->2->3->4->5->Null
    if head:
        dummy = LinkNode(float("-inf"))
        while head:
            # 先插1: dummy.next = head
            # dummy -> 1
            # 再插2: n = head.next, n.next = dummy.next
            # 2 -> 1, dummy -> 1
            # 连接: dummy.next = n
            # dummy -> 2 -> 1
            # 移位: head = head.next
            dummy.next, head.next, head = head, dummy.next, head.next
            return dummy.next

if __name__ == "__main__":
    head = linkList([1,2,3,4,5])
    reversed = reverseLink(head)