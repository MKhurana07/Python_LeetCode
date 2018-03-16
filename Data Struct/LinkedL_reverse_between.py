def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next
        
        # reverse the [m, n] nodes
        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next

class Linked_Node():
    def __init__(self,val):
        self.value = val 
        self.next = None
        
def reverse_mn(head,m,n):
    if m> n or m<0 or n<0:
        return False
    temp = temp1 = head
    while m >1:
        temp = head.next
    while n>0:
        temp1 = temp1.next
    temp.next = reverse(temp.next,temp1)
    while n-m>0:
        temp = temp.next
    temp.next = temp1
    return head

def reverse(head,tail):
    result = Linked_Node(-100)
    current = Linked_Node(-100)
    current = head
    while current != temp1:
        next = current.next
        current.next = result
        result = current
        current = next
    return result.next

a = Linked_Node(1)
b = Linked_Node(2)
c = Linked_Node(3)
d = Linked_Node(4)
e = Linked_Node(5)
a.next = b
b.next = c
c.next = d
d.next = e
res = reverse_mn(a,2,4)
while res.next !=None:
    print(res.value)
        
