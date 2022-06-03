from linked_list import Linked_list,print_LL

def cycle_LL(head):
    slow = head
    fast = head
    while slow != fast or slow is None or fast.next is None:
        slow = slow.next
        fast = fast.next.next
    if slow and fast:
        return True
    else:
        return False

link = Linked_list()
arr = [1,2,3,4]
temp = []
link.add_element(arr)
n = link.head
while n.next is not None:
    temp.append(n)
    n = n.next
n.next = temp[1]
#print_LL(link.head)
ans = cycle_LL(link.head)
print(ans)