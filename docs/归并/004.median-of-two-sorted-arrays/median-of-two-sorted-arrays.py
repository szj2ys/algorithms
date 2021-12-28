class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c = nums1 + nums2
        sc = sorted(c)
        if len(sc) % 2 == 0:
            return (sc[len(sc)//2] + sc[len(sc)//2 - 1]) /2
        else:
            return sc[len(sc)//2]