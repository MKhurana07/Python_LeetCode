class Dbl_ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         self.prev = None

def insert_beg(head, val):
    if not head:
        return
    node = Dbl_ListNode(val)
    head.prev = node
    node.next = head
    return node

def insert_after(head, val, after):
    if not head:
        return
    node = Dbl_ListNode(val)
    curr = head
    while head:
        if head.val == after:
            temp = head.next
            head.next = node
            node.next = temp
            node.prev = head
            temp.prev = node
            break
        head = head.next
    return curr

def insert_end(head, val):
    if not head:
        return
    curr = head
    while curr.next:
        curr = curr.next
    node = Dbl_ListNode(val)
    curr.next = node
    node.prev = curr
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
#res = insert_beg(a,7)
#res = insert_after(a,30,3)
res = insert_end(a,7)
while res:
    print(res.val)
    res = res.next
