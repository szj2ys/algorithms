class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        m = len(nums1)
        n = len(nums2)
        begin = 0
        end = m
        # 左半部分的最大值
        left_max = float("-inf")
        # 右半部分的最小值
        right_min = float("inf")
        while begin <= end:
            # 基于二分的方式求 i
            i = begin + (end - begin) // 2
            # 数组A长度为m，数组B长度n，总长度为偶数时，左半部分右半部分相等：
            # m - i + n - j = i + j
            # 总长度为奇数时，左半部分比右半部分多1个：
            # m - i + n - j + 1 = i + j
            # 统一奇数、偶数情况，得到j为：(m + n + 1) / 2 - i
            j = (n + m + 1) // 2 - i
            # 如果nums1[i - 1] > nums2[j]说明 i 取大了
            if i > 0 and j < n and nums1[i - 1]>nums2[j]:
                end = i - 1
            # nums2[j - 1] > nums1[i]，i 取小了
            elif j > 0 and i < m and nums2[j - 1]>nums1[i]:
                begin = i + 1
            #满足条件：nums1[i - 1] < nums2[j]，nums2[j - 1] < nums1[i]
            else:
                # 边界情况，数组A切分后左半部分为空 i == 0
                # 数组B 切分后左半部分为空 j == 0
                if i == 0:
                    left_max = nums2[j - 1]
                elif j == 0:
                    left_max = nums1[i - 1]
                # 求左半部分的最大值
                else:
                    left_max = max(nums1[i - 1],nums2[j - 1])
                # 总长度为奇数时，直接返回左半部分最大值即可
                if (n + m) % 2 == 1:
                    return float(left_max)
                # 边界情况，数组A 切分后，右半部分为空 i == m
                # 数组B 切分后，右半部分为空 j == n
                if i == m:
                    right_min = nums2[j]
                elif j == n:
                    right_min = nums1[i]
                # 求右半部分的最小值
                else:
                    right_min = min(nums1[i],nums2[j])
                # 总长度为偶数时
                return (left_max + right_min) / 2.0
        return 0.0

# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/duo-tu-xiang-jie-liang-chong-shi-xian-by-75f4/
# 时间复杂度：O(log min(m,n))
