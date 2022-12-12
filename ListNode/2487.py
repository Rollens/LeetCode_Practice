from ListNode import MakeList,ListNode

def removeNodes(head:ListNode) -> ListNode:
    
    start = cur = ListNode()
    cur.next = head.head
    while cur.next.next:
        if cur.val <= cur.next.val:
            start.next = cur
        cur = cur.next
    return start.next

if __name__ == '__main__':
    LeetCodeInput1 = [5,2,13,3,8]
    list1 = MakeList(LeetCodeInput1)
    removeNodes(list1)