# LeetCode 2 链表相加问题
# 输入两个链表, 返回链表的和
# 1 -> 2 -> 3 -> 4 (数字4321) + 0 -> 5 -> 2 (数字250) = 1 -> 7 -> 5 -> 4(数字4571)
class LinkNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def create(a):
    '''
    a = [1, 2, 3, 4]
    '''
    head = cur = LinkNode(0)
    for value in a:
        cur.next = LinkNode(value)
        cur = cur.next
    head = head.next
    return head

def printLinkNode(a):
    while a.next:
        print(a.value, end='->')
        a = a.next
    print(a.value)

# 写法1: 利用原有存储空间创建链表
def addSumv1(a, b):
    '''
    type: a: LinkNode
          b: LinkNode
    rtype: LinkNode
    n: a 和 b最小的位数
    '''
    acur = a
    bcur = b
    # 构造输出链表
    head = p = LinkNode(0)
    carry = 0
    while acur and bcur:
        val = acur.value + bcur.value + carry
        # 必须同时更新value和carry, 因此需要val
        value = val % 10
        carry = val // 10
        p.next = LinkNode(value)
        p = p.next
        acur = acur.next
        bcur = bcur.next
    #        a1 - a2 - a3 - a4 - a5 - a6 - a7 - a8
    #                            acur
    #        b1 - b2 - b3 - b4 - None
    #                            bcur
    # head - v1 - v2 - v3 - v4
    #                       p
    # 此时acur, bcur至少有一个指向了None, 而rcur指针指向第n位
    # lhead: 剩余链表的头指针
    lhead = lcur = acur or bcur
    if carry:
        if lhead:
            # 情况1: 455 + 12545 / 455 + 19545
            while carry and lcur.next:
                val = lcur.value + carry
                lcur.value = val % 10
                carry = val // 10
                lcur = lcur.next
            # a1 - a2 - a3 - a4 - a5 - a6 - a7 - a8
            #                     acur           lcur
            # 跳出循环有两种可能:
            # 1 carry = 0, 则将列表直接相连
            # 2 carry = 1, 则lcur指向最后一位
            p.next = lhead
            lcur.value = (lcur.value + carry) % 10
            # 情况2: 9455 + 545
            if not lcur.value:
                p.next.next = LinkNode(1)
        else:
            # 情况3: 455 + 545
            # 此时rcur指针指向第n位
            p.next = LinkNode(1)
    else:
        # 情况4, 455 + 536 / 1455 + 536, 无进位, 此时carry = 0
        # 位数不同则直接连起来
        if lcur:
            p.next = lcur
    printLinkNode(head.next)

# 写法二: 分配创造链表
def addSumv2(a, b):
    '''
    type: a: LinkNode
          b: LinkNode
    rtype: LinkNode
    n: a 和 b最小的位数
    '''
    acur = a
    bcur = b
    carry = 0
    p = head = LinkNode(0)
    while acur and bcur:
        print('a', acur.value)
        val = acur.value + bcur.value + carry
        # 必须同时更新value和carry, 因此需要val
        value = val % 10
        carry = val // 10
        p.next = LinkNode(value)
        acur = acur.next
        bcur = bcur.next
        p = p.next
    # 此时acur, bcur至少有一个指向了None, 而p指针指向第n位:
    #        a1 - a2 - a3 - a4 - a5 - a6 - a7 - a8
    #                            acur
    #        b1 - b2 - b3 - b4 - None
    #                            bcur
    # head - v1 - v2 - v3 - v4
    #                       p
    while acur:
        val = (acur.value + carry) % 10
        p.next = LinkNode(acur.value)
        carry = val // 10
        p = p.next
        acur = acur.next
    while bcur:
        val = (bcur.value + carry) % 10
        p.next = LinkNode(bcur.value)
        # 必须同时更新value和carry, 因此需要val
        carry = val // 10
        p = p.next
        bcur = bcur.next
    if carry == 1:
        p.next = LinkNode(1)
    printLinkNode(head.next)

a = create([5, 5, 4])
b = create([4, 4, 5])
addSumv1(a, b)
addSumv2(a, b)




