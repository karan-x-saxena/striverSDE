from linked_list import Linked_list,print_LL,Node

def reverse_sizeK(head,k):
    n = head
    lenght = 0
    while n is not None:
        n = n.next
        lenght = lenght+1
    count = 0
    dummy = Node(0)
    l = head
    prev = None
    while lenght >=k:
        if count == 0:
            dummy.next = l
            count = count+1
            prev = l
            l = l.next
            lenght = lenght - 1

        elif count == k:
            dummy.next.next = l.next
            l.next = prev
            count = 0
            dummy = dummy.next.next
            l = dummy.next.next
            lenght = lenght-1

        else:
            temp = l.next
            l.next = prev
            prev = l
            l = temp
            count = count+1
            lenght = lenght-1
    return head

link = Linked_list()
link.add_element([1,2,3,4,5,6,7,8])
ans = reverse_sizeK(link.head,3)
print_LL(ans)
