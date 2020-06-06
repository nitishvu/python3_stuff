'''
Reverse a singly linked list

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

A linked list can be reversed either iteratively or recursively. lets implement both.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Reverse single  linked list without recursion
    def reverseList(head: ListNode) -> ListNode:
        prev = None
        curr = head
        while (curr != None):
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        
        return prev
    # Reverse single  linked list with recursion
    def reverseList2(self,head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        parent = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return parent
        
    #print a single linked list
    def printList(head):
        while head != None:
            print(head.val)
            head = head.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
sobj = Solution()
result = sobj.reverseList2(node1)
Solution.printList(result)