[leetcode](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3] nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2] nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

## 分析
归并排序复杂度分析：

时间复杂度：O(M + N)，这里 M 和 N 分别是两个数组
的长度，代码只看了数组长度之和的一半，常数系数视
为 1。
空间复杂度：O(1)，我们没有借助其它的空间，使用到
的临时变量也只有常数个。
