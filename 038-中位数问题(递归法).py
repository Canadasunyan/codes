import numpy as np
class Solution(object):

    def getKth(self, A, B, k):
        len_a,len_b = len(A),len(B)
        # keep len(A) <= len(B)
        if len_a > len_b:
            return self.getKth(B, A, k)
        # when A is empty, return the kth minimal num in B
        if len_a == 0:
            return B[k - 1]
        # k: 挑出第几小的数
        # if k == 1, return the minimal num between A[0] and B[0]
        if k == 1:
            return min(A[0], B[0])
        pa = min(k // 2,len_a)
        # we have make len(B) > len(A), so pb always less than or equal to len(B) 
        pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:],B,k - pa)
        else:
            return self.getKth(A,B[pb:],k - pb)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return None
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.getKth(nums1, nums2, n // 2 + 1)
        else:
            return (self.getKth(nums1, nums2, n // 2) + self.getKth(nums1, nums2, n // 2 + 1) ) * 0.5

sol = Solution()
a = [1,3,5,7,9,11,12,13,14,15,17]
b = [12,14]
true_val = np.median(a + b)
p = sol.findMedianSortedArrays(a, b)
print(p == true_val)