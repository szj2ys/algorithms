[leetcode](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3] nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2] nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

## [分析一](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/)
## [分析二](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/he-bing-yi-hou-zhao-gui-bing-guo-cheng-zhong-zhao-/)
如果对时间复杂度的要求有 $$log$$，通常都需要用到二分
查找，这道题也可以通过二分查找实现。
根据中位数的定义，当 $$m+nm+n$$ 是奇数时，中位数
是两个有序数组中的第 $$(m+n)/2(m+n)/2$$ 个元素，
当 $$m+nm+n$$ 是偶数时，中位数是两个有序数组
中的第 $$(m+n)/2(m+n)/2$$ 个元素和
第 $$(m+n)/2+1(m+n)/2+1$$ 个元素的平均值。
因此，这道题可以转化成寻找两个有序数组中的第 $$k$$ 
小的数，其中 $$k$$ 为 $$(m+n)/2(m+n)/2$$ 
或 $$(m+n)/2+1(m+n)/2+1$$。

假设两个有序数组分别是 $$\text{A}A$$ 和 $$\text{B}B$$。要找到第 $$k$$ 个元素，我们可以比较 \text{A}[k/2-1]A[k/2−1] 和 \text{B}[k/2-1]B[k/2−1]，其中 // 表示整数除法。由于 \text{A}[k/2-1]A[k/2−1] 和 \text{B}[k/2-1]B[k/2−1] 的前面分别有 \text{A}[0\,..\,k/2-2]A[0..k/2−2] 和 \text{B}[0\,..\,k/2-2]B[0..k/2−2]，即 k/2-1k/2−1 个元素，对于 \text{A}[k/2-1]A[k/2−1] 和 \text{B}[k/2-1]B[k/2−1] 中的较小值，最多只会有 (k/2-1)+(k/2-1) \leq k-2(k/2−1)+(k/2−1)≤k−2 个元素比它小，那么它就不能是第 kk 小的数了。

因此我们可以归纳出三种情况：

如果 $$\text{A}[k/2-1] < \text{B}[k/2-1]A[k/2−1]<B[k/2−1]$$，则比 $$\text{A}[k/2-1]A[k/2−1]$$ 小的数最多只有 \text{A}A 的前 k/2-1k/2−1 个数和 \text{B}B 的前 k/2-1k/2−1 个数，即比 \text{A}[k/2-1]A[k/2−1] 小的数最多只有 k-2k−2 个，因此 \text{A}[k/2-1]A[k/2−1] 不可能是第 kk 个数，\text{A}[0]A[0] 到 \text{A}[k/2-1]A[k/2−1] 也都不可能是第 kk 个数，可以全部排除。

如果 $$\text{A}[k/2-1] > \text{B}[k/2-1]A[k/2−1]>B[k/2−1]$$，则可以排除 $$\text{B}[0]B[0]$$ 到 $$\text{B}[k/2-1]B[k/2−1]$$。

如果 $$\text{A}[k/2-1] = \text{B}[k/2-1]A[k/2−1]=B[k/2−1]$$，则可以归入第一种情况处理。

![](https://assets.leetcode-cn.com/solution-static/4/4_fig1.png)

