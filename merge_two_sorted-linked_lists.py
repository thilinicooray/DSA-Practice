# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        #merged = None
        if head1.val < head2.val:
            cur1 = list1
            list1 = head1.next
            cur1.next = None
            merged = cur1

        else:
            cur2 = list2
            list2 = head2.next
            cur2.next = None
            merged = cur2

        cur1 = list1
        cur2 = list2
        cur_merge = merged

        while cur1 and cur2:
            if cur1.val < cur2.val:
                list1 = cur1.next
                cur1.next = None
                cur_merge.next = cur1
                cur_merge = cur_merge.next
                cur1 = list1

            else:
                list2 = cur2.next
                cur2.next = None
                cur_merge.next = cur2
                cur_merge = cur_merge.next
                cur2 = list2

        if cur1:
            #list1 = None

            cur_merge.next = cur1

        else:
            #list2 = None

            cur_merge.next = cur2

        return merged

        
        