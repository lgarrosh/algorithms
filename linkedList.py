class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __int__(self):
        if not self.head:
            return None
        i = 0
        last_node = self.head
        while last_node:
            i *= 10
            i += last_node.val
            last_node = last_node.next
        return i
    
    def __reversed__(self) -> ListNode:
        reversed_list = LinkedList()
        last_node = self.head
        if not last_node:
            return None
        while last_node:
            next_node = last_node.next
            last_node.next = reversed_list.head
            reversed_list.head = last_node
            last_node = next_node
        return reversed_list.head
        

    def linkedList(numb):
        my_str = str(numb)
        return_value = LinkedList()

        for i in my_str:
            return_value.append(int(i))
        return return_value


    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print("None")