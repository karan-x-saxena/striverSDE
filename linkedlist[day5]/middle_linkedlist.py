from linked_list import Linked_list,print_LL

def middle_element(head):
    fast = head
    slow = head
    while fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

link = Linked_list()
link.add_element([1,2,3,4,5])
ans = middle_element(link.head)
print_LL(ans)
