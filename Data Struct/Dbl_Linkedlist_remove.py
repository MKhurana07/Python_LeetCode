class Dbl_ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         self.prev = None

def remove_front(head):
    if not head:
        return
    head = head.next
    head.prev = None
    return head

def remove_end(head):
    if not head:
        return
    curr = head
    while curr.next:
        curr = curr.next
    curr.prev.next = None
    curr.prev = None
    return head

def remove_n(head,val):
    if not head:
        return
    curr = head
    while curr:
        if curr.val == val:
            curr.next.prev = curr.prev
            curr.prev.next = curr.next
            break
        curr=curr.next
    return head


a = Dbl_ListNode(1)
b = Dbl_ListNode(2)
c = Dbl_ListNode(3)
d = Dbl_ListNode(4)
e = Dbl_ListNode(5)
a.next = b
b.prev = a
b.next = c
c.prev = b
c.next = d
d.prev = c
d.next = e
e.prev = d
e.next = None
#res = remove_end(a)
res = remove_front(a)
#res = remove_n(a,4)
while res:
    print(res.val)
    res = res.next
