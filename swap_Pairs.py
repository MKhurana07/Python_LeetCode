class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
def swapPairs(head):
    prev_head = ListNode(-1)
    prev_head = head.next
    while head!=None and head.next!=None:
        temp = head.next.next
        head.next.next = temp.next
        swap = head.next
        swap.next = head
        head.next = temp
        head = temp
    return prev_head
a = ListNode(1)
b =  ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = None
e.next = None
final = swapPairs(a)
while final.next != None:
    print(final.val)
    final = final.next

        
