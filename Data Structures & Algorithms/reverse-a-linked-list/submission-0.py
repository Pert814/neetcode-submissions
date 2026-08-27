# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head # curr當作頭
        pre = None #虛擬頭 目的: curr -> pre
        while curr is not None:
            nxt = curr.next #先備份 原本的curr.next
            curr.next = pre # curr -> pre
            pre = curr
            curr = nxt
        return pre

# N(pre) A(curr) -> B(nxt) -> C -> ...
# N <- A(pre) B(curr) -> C(nxt) -> ...            
# N <-A <- B C->...            
# ...
# N <- A <- B <- C ... <- Z(pre) 
            

            

        
        