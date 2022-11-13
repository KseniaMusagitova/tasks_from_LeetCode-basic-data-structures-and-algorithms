# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def removeElements(self, head, val):

        prev = None
        curr = head
        while curr:
            if curr.val == val:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head



sol = Solution()
print(sol.removeElements(head = [1,2,6,3,4,5,6], val = 6))


# head = [1,2,6,3,4,5,6]
# val = 6
#
# for element in head:
#     if element == val:
#         head.remove(element)
# print(head)

