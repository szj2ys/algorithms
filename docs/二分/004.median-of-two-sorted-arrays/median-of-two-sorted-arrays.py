class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        total = len(nums1) + len(nums2)
        # 如果A数组长度+B数组长度total是奇数，则找total/2+1小的元素
        # 即为中位数
        if total % 2 == 1:
            midIndex = total / 2 + 1
            res = self.getKthElement(nums1, nums2, midIndex)
            return float(res)
        # 否则，找total/2，total/2+1这两个元素
        else:
            midIndex_1 = total / 2
            midIndex_2 = total / 2 + 1
            a = self.getKthElement(nums1, nums2, midIndex_1)
            b = self.getKthElement(nums1, nums2, midIndex_2)
            return (a + b) / 2.0

    def getKthElement(self,nums1, nums2, k):
        len1 = len(nums1)
        len2 = len(nums2)
        index1 = 0
        index2 = 0
        while True:
            # 边界情况，当index1越界时，直接返回nums2的第k小元素
            if index1 == len1:
                return nums2[index2 + k -1]
            # 边界情况，当index2越界时，直接返回nums1的第k小元素
            if index2 == len2:
                return nums1[index1 + k - 1]
            # 边界情况，k等于1时，返回nums1第一个元素和nums2第一个元素较小者
            if k == 1:
                return min(nums1[index1], nums2[index2])
            new_index1 = min(index1 + k / 2, len1) - 1
            new_index2 = min(index2 + k / 2, len2) - 1
            pivot1 = nums1[new_index1]
            pivot2 = nums2[new_index2]
            # 比较nums1[k/2-1]和nums2[k/2-1]
            # 如果nums1的小，则忽略掉nums1[0] - nums1[k/2-1]这些元素
            # 再更新 k，k 要减去忽略掉的那些元素，index1也要更新，待下轮使用
            if pivot1 <= pivot2:
                k -= (new_index1 - index1 + 1)
                index1 = new_index1 + 1
            # 如果nums2的小，则忽略掉nums2[0] - nums2[k/2-1]这些元素
            # 再更新 k，k 要减去忽略掉的那些元素，index2也要更新，待下轮使用
            else:
                k -= (new_index2 - index2 + 1)
                index2 = new_index2 + 1






