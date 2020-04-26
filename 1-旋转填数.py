# [[ 1. 20. 19. 18. 17. 16.]
#  [ 2. 21. 32. 31. 30. 15.]
#  [ 3. 22. 33. 36. 29. 14.]
#  [ 4. 23. 34. 35. 28. 13.]
#  [ 5. 24. 25. 26. 27. 12.]
#  [ 6.  7.  8.  9. 10. 11.]]

# 设置指针指明方向
# 先确定方向再往前进一步
import numpy as np
size = eval(input('Please type the size of the matrix!'))
if type(size) != int:
    raise TypeError
matrix = np.zeros((size, size))

i = 0
j = 0
for value in range(size*size):
    matrix[i][j] = value + 1
    if i + j < size - 1 and j <= i + 1:
        # 0: 向下
        orient = 0
    if i + j >= size - 1 and i > j:
        # 1: 向右
        orient = 1
    if i + j > size - 1 and i <= j:
        # 2: 向上
        orient = 2
    if i + j <= size - 1 and j >= i + 2:
        # 3: 向左
        orient = 3
    # 先确定方向，再往前走一步
    if orient == 0:
        i += 1
    if orient == 1:
        j += 1
    if orient == 2:
        i -= 1
    if orient == 3:
        j -= 1
print(matrix)






