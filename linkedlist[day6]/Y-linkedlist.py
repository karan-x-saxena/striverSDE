from linked_list import Linked_list, print_LL

def Y_linkedlist(head1,head2):
    dummy1 = head1
    dummy2 = head2
    while dummy1 != dummy2:
        if dummy1 is None:
            dummy1 = head2
        dummy1 = dummy1.next
        dummy2 = dummy2.next