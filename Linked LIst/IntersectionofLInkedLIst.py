# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        currentA=A
        currentB=B

        while currentA and currentB:
            currentB=currentB.next
            currentA=currentA.next
        if currentA is None:
            first=B
            firstcurrent=currentB
            second=A
        else:
            first=A
            firstcurrent=currentA
            second=B
        while(firstcurrent):
            first=first.next
            firstcurrent=firstcurrent.next
        while first is not None:
            if first is second:
                return first
            first=first.next
            second=second.next
        return None



