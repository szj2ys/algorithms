# *_*coding:utf-8 *_*
from __future__ import absolute_import, division, print_function
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur:
                return pre
            res  = recur(cur.next, cur)
            cur.next = pre
            return res
        return recur(head, None)


if __name__ == '__main__':
    solution = Solution()
    ll = [1,2,3,4,5]
    ll = ListNode(ll)
    res = solution.reverseList(ll)
    print(list(res))
