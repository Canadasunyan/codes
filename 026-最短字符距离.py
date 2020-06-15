# 最小文本距离问题
# 输入一个含0, 1, -1的序列, 返回1和-1之间的最小距离
def minDistance(ls):
    """
    type(series): List[int]
    rtype: int
    """
    i, loc_1, loc_2 = 0, None, None
    dist = float('inf')
    while i < len(ls):
    # 先定位到第一个1或-1
    if ls[i] == 1:
        loc_1 = i
    if ls[i] == -1:
        loc_2 = i
    # 1和-1都存在时更新distance
    if loc_1 and loc_2:
        dist = min(dist, abs(loc_1-loc_2))
    return dist


