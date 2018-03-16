class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def insert_N(head, val, node):
    if not head:
        return 0
    curr = head.next
    while curr:
        if curr.val == val:
            node.next = curr.next
            curr.next = node
            break
        curr = curr.next
    return head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(7)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = None
f.next = None
res = insert_N(a,3,f)
while res:
    print(res.val)
    res = res.next
        
            
