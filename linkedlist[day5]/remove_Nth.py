from linked_list import Linked_list,print_LL

def remove_Nth(head,n):
    fast = head
    slow = head
    for i in range(n):
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next

    temp = slow.next.next
    slow.next = temp
    return head

link = Linked_list()
arr = [7,6,9,4,13,2,8]
n = 6
link.add_element(arr)
ans = remove_Nth(link.head,n)
print_LL(ans)