class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = spot = ListNode()
        answer.next = l1
        if l1 or l2:
            return l1 or l2
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                spot_copy = spot.next
                spot.next = l2
                l2_copy = l2.next
                l2.next = spot_copy
                l2 = l2_copy
            spot = spot.next
        spot.next = l1 or l2
        return answer.next
    ```
    연결리스트 뭔가 이해가 어렵다
    ```