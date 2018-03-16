class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def mergeKLists(l):
    merge =[]
    for i in l:
        while i:
            merge.append(i.val)
            i = i.next
    merge.sort()
    merged_list = ListNode(-1)
    prev = ListNode(-1)
    prev.next = merged_list
    for i in merge:
        merged_list.next = ListNode(i)
        merged_list = merged_list.next
    return prev.next.next

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
a2 = ListNode(1)
b2 = ListNode(2)
c2 = ListNode(3)
d2 = ListNode(4)
e2 = ListNode(5)
a2.next = b2
b2.next = c2
c2.next = d2
d2.next = e2
e2.next = None

final = mergeKLists([a,a1,a2])
print(final)
while final.next != None:
    print(final.val)
    final = final.next
