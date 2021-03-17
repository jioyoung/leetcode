#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 合并 链表
        h = []
        for i, oneList in enumerate(lists):
            if oneList is not None:
                heapq.heappush(h, (oneList.val, i,  oneList))
                # i needs to be added 
                # since if there 
        dummy = head = ListNode(0)
        while h:
            _, i, oneList = heapq.heappop(h)
            head.next = oneList
            head = head.next
            if oneList.next is not None:
                heapq.heappush(h, (oneList.next.val, i, oneList.next))
        return dummy.next

# @lc code=end

