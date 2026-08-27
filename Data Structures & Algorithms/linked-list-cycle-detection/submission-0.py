# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next:
            fast, slow = head.next, head
        else:
            return False

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # if fast.val = slow.val: 這樣寫會錯，因爲元素可能重複
            if fast == slow:
                return True
        return False 
        