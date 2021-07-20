
class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # hash用于建立数值到下标的映射
    hash = {}
    # 循环nums数值
    for i, num in enumerate(nums):
      if target - num in hash:
        return [hash[target - num], i]
      hash[num] = i  # 添加映射
    return [-1, -1]  # 无解的情况

# 时间复杂的 O(n)

