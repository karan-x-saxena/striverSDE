from linked_list import Linked_list, print_LL

def Reverse_linkedlist(head):
    temp = None
    while head is not None:
        temp1 = head.next
        head.next = temp
        temp = head
        head = temp1
    return temp

link = Linked_list()

arr = [3,6,8,10]
link.add_element(arr)
print_LL(link.head)
a = Reverse_linkedlist(link.head)
print_LL(a)