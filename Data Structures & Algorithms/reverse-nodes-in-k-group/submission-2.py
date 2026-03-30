# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) ->ListNode:
        dummy=ListNode(0, head)
        groupPrev=dummy
        
        while True:
            kth=self.getKthNode(groupPrev ,k)
            if not kth:
                break
            prev=groupNext=kth.next
            curr=groupPrev.next

            while curr!=groupNext:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            tmp=groupPrev.next
            groupPrev.next=kth
            groupPrev=tmp

        return dummy.next

    def getKthNode(self, node, k):
        while node and k>0:
            node=node.next
            k-=1
        return node