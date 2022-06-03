class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def push_element(self,x):
        new = Node(x)
        if self.head is None:
            self.head = new
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new

    def add_element(self,arr):
        for i in arr:
            self.push_element(i)

def print_LL(head):
    if head is None:
        print("linked list is empty!")
    else:
        n = head
        while n is not None:
            if n.next is None:
                print(n.data)
            else:
                print(n.data,end=" ")
            n = n.next

if __name__ == '__main__':
    a = Linked_list()
    arr = [1,2,3,4,5,6]
    a.add_element(arr)
    print_LL(a.head)