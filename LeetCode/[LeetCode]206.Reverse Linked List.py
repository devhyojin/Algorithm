# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None
        current = head
        #현재 위치가 null값이 아닐 때까지 tail마저 벗어나버린 상태가 아닐 때까지만 진행
        while current:
            #다음 위치의 값을 저장해주자.
            next_up = current.next 
            #리스트의 시작값의 방향키를 바꿔주자
            current.next = prev
            #다음 단계로 넘어가기 위해, 이전 위치와, 현재 위치값을 재설정해주자.
            prev = current
            current = next_up
        #리스트의 시작점 또한 바꿔주자.
        head = prev
        
        return head