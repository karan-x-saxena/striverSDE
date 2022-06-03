from linked_list import Linked_list, print_LL,Node

def add_as_ll(head1,head2):
    carry = 0
    l1 = head1
    l2 = head2
    dummy = Node(0)
    temp = dummy
    while l1 or l2 or carry == 1:
        sum = 0
        if l1 and l2:
            sum = l1.data + l2.data
        elif l1:
            sum = l1.data
        elif l2:
            sum = l2.data
        sum = sum+carry
        if sum//10 == 1:
            new = Node(sum%10)
            carry = 1
            dummy.next = new
            dummy = dummy.next
        else:
            new = Node(sum)
            carry = 0
            dummy.next = new
            dummy = dummy.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return temp.next

link1 = Linked_list()
link2 = Linked_list()
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
link1.add_element(l1)
link2.add_element(l2)
ans = add_as_ll(link1.head,link2.head)
print_LL(ans)