class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def addAtHead(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def deleteAtIndex(self, index):
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for i in range(index-1):
                curr = curr.next
                if not curr:
                    return
            curr.next = curr.next.next

    def get(self, index):
        if not self.head:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
            if not curr:
                return -1
        return curr.val