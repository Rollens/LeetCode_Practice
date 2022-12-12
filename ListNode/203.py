from ListNode import MakeList,ListNode

LeetCodeInput1 = [1,2,6,3,4,5,6]
#LeetCodeInput2 = [1,3,4]

list1 = MakeList(LeetCodeInput1)
#list2 = MakeList(LeetCodeInput2)

def removeElements(head:ListNode,val:int)->ListNode:
    dummy = ListNode(-1,head)
    prev = dummy
    while head:
        if head.val != val:
            prev = head
        else:
            prev.next = head.next
        head = head.next
    return dummy.next

if __name__ == '__main__':
    output=removeElements(list1.head,6)