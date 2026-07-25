# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        curr=head
        lenght=0
        while curr:
            lenght+=1
            curr=curr.next
        x=lenght-n
        curr=head
        if x == 0:
            return head.next
        for i in range(x):
            if i==x-1:
                curr.next=curr.next.next
                break
            curr=curr.next
        return head
        