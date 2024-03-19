from typing import Optional
from linkedList import LinkedList
from linkedList import ListNode
from decoratorFunction import decorator_function

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = LinkedList(reversed(LinkedList(l1)))
        list2 = LinkedList(reversed(LinkedList(l2)))
        sum = int(list1) + int(list2)
        return reversed(LinkedList.linkedList(sum))


if __name__ == '__main__':
    sol = Solution()
    list1 = LinkedList.linkedList(56)
    list2 = LinkedList.linkedList(5)

    run_func = decorator_function(sol.addTwoNumbers)
    print(run_func(list1.head, list2.head))


    # result = sol.addTwoNumbers(list1.head, list2.head)
    # list_test = LinkedList(result)
    # list_test.display()
