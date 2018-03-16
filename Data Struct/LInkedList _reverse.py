class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
def reverse_iterative(head):
    result = ListNode(-100)
    current = ListNode(-100)
    current = head
    while current:
        next = current.next
        current.next = result
        result = current
        current = next
    return result.next.val

def reverse_recursive(head):
    if not head:
        return
    first = head
    rest = head.next
    if rest == None:
        return
    reverse_recursive(rest)
    first.next.next = first
    first.next = None
    return rest.val

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
print(reverse_recursive(a))

