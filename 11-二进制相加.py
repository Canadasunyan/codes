# Leetcode27. 二进制问题
# 所有进制问题都要从个位往前算
def addBinary(a, b):
    '''
    a, b: string of binary codes
    a: '1001010'
    b: '10100100'
    '''
    # carry: 是否进一位, value: 当前位的值
    carry = value = 0
    result = ''
    for i in range(max(len(a), len(b))):
        if i < len(a):
            value += int(a[-i - 1])
        if i < len(b):
            value += int(b[-i - 1])
        # value = 2则进位, value退回0, 否则carry与value不变
        carry, value = value // 2, value % 2
        result += str(value)
        value = carry
    if carry:
        result += '1'
    return result[::-1]

print(addBinary('1001010', '10100100'))