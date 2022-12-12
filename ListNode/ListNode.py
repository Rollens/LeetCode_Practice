class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MakeList:
    def __init__(self,data=None) -> None:
        dummy = cur = ListNode()
        if data:
            for i in data:
                new = ListNode(i)
                cur.next = new
                cur = new
            self.head = dummy.next
        else:
            return 
    def display(self):
        output = []
        cur = self.head
        while cur:
            output.append(cur.val)
            cur = cur.next
        print(output)
