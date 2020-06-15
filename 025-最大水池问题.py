# 最大水池问题
# 给定每个木棒的长度, 输出任意两个木棒间所能围住水的最大面积
def maxArea(height):
    # 初始化水槽面积
    max_area = 0
    # 初始化左右角标
    left = 0
    right = len(height) - 1
    while left < right:
        h1 = height[left]
        h2 = height[right]
        area = min(left, right) * (right - left)
        # 获得更大面积则更新面积
        max_area = area if area > max_area else max_area
        if h1 < h2:
            # 如果左棍右侧的长度更低, 肯定围不成最大面积
            while height[left] <= h1:
                left += 1
        else:
            # 如果右棍左侧的长度更低, 肯定围不成最大面积
            while height[right] <= h2:
                right -= 1
    return max_area

m = maxArea([1,2,3,4,5,6,7,8,7,6,5,4,3,2,1])


