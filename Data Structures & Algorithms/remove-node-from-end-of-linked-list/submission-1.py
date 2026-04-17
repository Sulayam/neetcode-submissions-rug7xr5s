# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        leftNode=dummy
        rightNode=head

        while n>0:
            rightNode=rightNode.next
            n-=1
        
        while rightNode:
            rightNode=rightNode.next
            leftNode=leftNode.next
        
        leftNode.next=leftNode.next.next

        return dummy.next
        