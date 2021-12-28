[leetcode](https://leetcode-cn.com/problems/add-two-numbers/)

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg)
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

## 分析

为什么可以用递归？
如图所示，可以直观看到只需将各个单位的位置的值加起来。
我们只需要考虑进位就可以了。


要考虑两点：

- 1.递归函数交付给上层什么？
没错，交付的是两节点相加后的值（sum%10）
- 2.递归函数的终止条件是什么？
当指针都为Null 且 进位carry为0时 return null









