# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        sentinel = ListNode(0, head)
        current = head.next
        prev = head
        while current and current.next:
            if current and current.val > prev.val and current.next.val != current.val:
                # move both prev and current
                current = current.next
                prev = prev.next
            elif current and (current.val == prev.val or current.next.val == current.val):
                # check until current.next > current
                while current.next and current.next.val == current.val:
                    current = current.next
                if prev == head:
                    if current.next and prev.val == current.val:
                        head = current.next
                        prev = head
                        current = prev.next
                    elif current.next and prev.val < current.val:
                        temp = current.next
                        prev.next = temp
                    else:
                        prev.next = None
                        current = prev
                elif prev != head:
                    if current.next:
                        temp = current.next
                        prev.next = temp
                        current = prev.next
                    else:
                        prev.next = None
        return head

    def deleteDuplicatesSentinel(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        
        prev = sentinel
        
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
                
            head = head.next
        return sentinel.next

    def print_list(self, head):
        current = head.next
        if not current:
            print("It is none")
        while current:
            print(current.val, end=" ")
            current = current.next
        return


if __name__ == "__main__":

    # build linked list
    head = ListNode()
    current = head
    inp = [1,1,1,1,1,2,3,4,4,4,4,4,5,6,7,8,8,8,8,9,9,10]
    for n in inp:
        current.next = ListNode(n)
        current = current.next

    solution = Solution()
    solution.print_list(solution.deleteDuplicatesSentinel(head))
