# 最长回文字符串
# 给定某字符串, 输出最长回文字符串
def getlongestpalindrome(s, l, r):
    # 情况1
    # s = 'abcbade', l = r = 2
    # 'c' = 'c', l = 1, r = 3
    # 'b' = 'b', l = 0, r = 4
    # 情况2
    # s = 'abccbade', l = 2, r = 3
    # 'c' = 'c', l = 1, r = 4
    # 'b' = 'b', l = 0, r = 5
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1: r]
def longestPalindrome(s):
    # 初始化字符串
    p = ''
    # 以每个字符为中心, 分两种情况扩展回文字符串
    for i in range(len(s)):
        str1 = getlongestpalindrome(s, i, i)
        str2 = getlongestpalindrome(s, i, i+1)
        max_str = max(len(str1), len(str2), len(p))
        p = p if len(p) == max_str else str1 if len(str1) == max_str else str2
    return p

if __name__ =="__main__":
    print(longestPalindrome('abcdcbade'))

