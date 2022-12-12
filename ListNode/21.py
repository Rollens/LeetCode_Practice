from ListNode import MakeList,ListNode

LeetCodeInput1 = [1,2,4]
LeetCodeInput2 = [1,3,4]

list1 = MakeList(LeetCodeInput1)
list2 = MakeList(LeetCodeInput2)

def mergeTwoLists(list1:ListNode, list2:ListNode) -> ListNode:
    cur = head = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 , cur = list1.next , list1
        else:
            cur.next = list2
            list2 , cur = list2.next , list2
        if list1 or list2:
            cur.next = list1 if list1 else list2
    return head.next

if __name__ == '__main__':
    output=mergeTwoLists(list1.head,list2.head)