# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        #take out the even nodes and then append them

        oddhead = head
        odd = head
        evenhead = head.next
        even = head.next
        
        while even is not None:
            odd.next = even.next
            
            if odd.next is not None:
                odd = odd.next
            
            even.next = odd.next
            even = even.next
            
        odd.next = evenhead
        
        return oddhead