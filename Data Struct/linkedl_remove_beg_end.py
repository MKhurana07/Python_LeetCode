class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def removeNthfrombeg(head, n):
    for i in range (1,n-1):
        head = head.next
    temp = head.next
    head.next = temp.next
    return temp.val

def removeNthfromend(head,n):
    ptr = head
    length = 1
    while ptr.next != None :
        ptr = ptr.next
        length = length + 1
    print(length)    
    for i in range (0,length-n-1):
        head = head.next
    temp = head.next
    head.next = temp.next
    return temp.val

def remove_node(head, val):
     if not head:
          return
     curr = head
     if head.val == val:
          head = head.next
          return head
     while curr:
          if curr.next.val == val:
               curr.next = curr.next.next
               break
          curr = curr.next
     return head


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
##print(removeNthfromend(a,2))
##print(removeNthfrombeg(a,2))
res = remove_node(a,3)
while res:
     print(res.val)
     res = res.next
