class Solution:
  def twoSum(self, nums, target):
    sorted_nums = sorted(nums)
    left, right = 0, len(nums) - 1

    while left < right:
      if sorted_nums[left] + sorted_nums[right] == target:
        i = nums.index(sorted_nums[left])
        j = nums.index(sorted_nums[right])

        if i == j:  ##两个重复的数字时候，index只能返回最小的指针
          k = nums[i + 1:].index(sorted_nums[right]) + i + 1
          return [i, k]
        elif i < j:
          return [i, j]
        else:
          return [j, i]

      elif sorted_nums[left] + sorted_nums[right] < target:
        left += 1
      else:
        right -= 1

    return [-1, -1]  # 无解的情况

# 使用双指针算法，时间复杂度O(nlogn) ，空间复杂度O(n)
# ## 双指针
# 先对数组拷贝，然后对数组排序，在排序后的数组中利用双指针从左右向中间寻找
#
# - 如果numbers[i] + numbers [j] == target 说明找到答案
# - 如果numbers[i] + numbers [j] < target 说明当前和比答案小。左指针右移
# - 如果numbers[i] + numbers [j] > target 说明当前和比答案大。右指针左移
#
# 然后在拷贝数组中找到对应numbers[i]和numbers[j] 的下标，对这两个下标排个序

