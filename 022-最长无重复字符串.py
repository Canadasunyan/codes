# 最长无重复字符串
# 给定一个字符串, 输出无重复的子串的最大长度
# 建立字典记录每个字符出现的最后位置, 设置指针指向每次扫描的起点
def maxLength(string):
    """
    string: str
    rtype: int
    """
    # 设置字典记录每个字符出现的最后位置
    dictionary = {}
    start = -1
    max_length = 0
    for i in string:
        # 字符已经存在于字典中, 且当前的字符串包含了该字符
        # eg. a    b   c   d   e   b    e   f
        #     |    |               |
        #    s=0   1               i
        if i in dictionary and dictionary[i] > start:
            # 开始指针后移至重复字符位置, 从start后一位字符开始计算字符串长度
            start = dictionary[string[i]]
            dictionary[string[i]] = i
        # eg. a    b   c   d   e   b    e   f
        #          |               |
        #         s=1              5
        # 如果不在字典中则添加到字典, 更新最大值
        # 只有添加字典时最大长度才可能增加
        else:
            dictionary[string[i]] = i
            if i - start > max_length:
                max_length = i - start
    return max_length



