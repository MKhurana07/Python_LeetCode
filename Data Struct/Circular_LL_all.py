class Circ_ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         self.prev = None

def insert_beg(head, val):
    if not head:
        return
    node = Circ_ListNode(val)
    node.prev = head.prev
    node.next = head
    return node

def insert_at_N(head, val, n):
    if not head:
        return
    node = Circ_ListNode(val)
    curr = head
    while curr:
        if curr.val == n:
            temp = curr.next
            curr.next = node
            node.prev = curr
            node.next = temp
            break
        curr = curr.next
    return head

def remove_N(head,n):
    if not head:
        return
    curr = head
    while True:
        if curr.val == n:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            break
        curr = curr.next
        if curr == head:
            break
    return head

def reverse(head):
    if not head:
        return
    curr = head
    while True:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        curr = curr.prev
        if curr == head:
            break
    return temp.prev

a = Circ_ListNode(1)
b = Circ_ListNode(2)
c = Circ_ListNode(3)
d = Circ_ListNode(4)
e = Circ_ListNode(5)
a.next = b
b.prev = a
b.next = c
c.prev = b
c.next = d
d.prev = c
d.next = e
e.prev = d
e.next = a
#res = insert_beg(a,7)
#res = insert_after(a,30,3)
res = reverse(a)
while True:
    print(res.val)
    res = res.next
    if res == a:
        break
