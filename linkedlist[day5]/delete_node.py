from linked_list import Linked_list,print_LL

def delete_node(head):
    head.data = head.next.data
    temp = head.next.next
    head.next = temp

