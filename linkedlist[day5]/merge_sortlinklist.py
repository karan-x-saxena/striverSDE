from linked_list import Linked_list,print_LL

def merge_sorted(head1,head2):
    ll1 = head1
    ll2 = head2
    back = None
    res = None
    while ll1 and ll2:
        if ll1.data >= ll2.data:
            temp = ll2.next
            if back is None:
                ll2.next = ll1
                back = ll2
                res = ll2
                ll2 = temp
            else:
                ll2.next = ll1
                back.next = ll2
                back = back.next
                ll2 = temp
        else:
            if back is None:
                back = ll1
            else: back = back.next
            ll1 = ll1.next

    if ll2 is not None:
        back.next = ll2
    if res is None:
        return head1
    else: return res


link1 = Linked_list()
link2 = Linked_list()
l1 = [3,7,10]
l2 = [1,2,5,8,10]
link1.add_element(l1)
link2.add_element(l2)
ans = merge_sorted(link1.head,link2.head)
print_LL(ans)