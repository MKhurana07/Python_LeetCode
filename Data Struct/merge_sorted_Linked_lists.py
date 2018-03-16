class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def mergeTwoLists(l1, l2):
    prev = ListNode(-1000)
    head = ListNode(-1000)
    head = prev
    while l1!=None and l2!= None:
        if l1.val >= l2.val:
            prev.next = l2
            prev = l2
            l2= l2.next
        else:
            prev.next = l1
            prev = l1
            l1 = l1.next

    if l1 == None:
        while l2 != None:
            prev.next = l2
            prev = l2
            l2 = l2.next
    else:
        while l1 != None:
            prev.next = l1
            prev = l1
            l1 = l1.next
    return head.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = None
a1 = ListNode(1)
b1 = ListNode(2)
c1 = ListNode(3)
d1 = ListNode(4)
e1 = ListNode(5)
a1.next = b1
b1.next = c1
c1.next = d1
d1.next = e1
e1.next = None

a2 = mergeTwoLists(a,a1)
while a2.next != None:
    print(a2.val)
    a2 = a2.next
