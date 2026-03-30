# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=[]

        for outer in lists:
            current=outer
            while current:
                res.append(current.val)
                current=current.next
        res=sorted(res)
        print(f"res:{res}")

        current=dummy=ListNode(-1)

        for number in res:
            current.next=ListNode(number)
            current=current.next

        return dummy.next