class Dbl_ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         self.prev = None
         
def reverse(head):
    if not head:
        return
    curr = head
    
    while curr:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        curr = curr.prev
    return temp.prev


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
res = reverse(a)
while res:
    print(res.val)
    res = res.next
