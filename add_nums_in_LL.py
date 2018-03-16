class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def addTwoNumbers( l1, l2):
        l1 = l1[::-1]
        l2 = l2[::-1]
        for i in range(max(len(l2),len(l1))):
            if l2[i] and l1[i]:
                answ[i] = l2[i] + l1[i]
            elif l2[i]:
                answ[i] = l2[i]
            elif l1[i]:
                answ[i] = l1[i]

def addTwoLists(l1,l2):
    dummy = curr = ListNode(0)
    carry = 0
    while l1 or l2 :
        if l1:
            carry = carry + l1.val
            l1=l1.next
        if l2:
            carry = carry + l2.val
            l2 = l2.next
        ##carry, val = divmod(carry,10)
        curr.next = ListNode(carry%10)
        curr = curr.next
        carry= carry//10
    return dummy.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a1 = ListNode(1)
b1 = ListNode(2)
c1 = ListNode(3)
a.next =b
b.next =c
a1.next =b1
b1.next =c1
a.next =b
l = addTwoLists(a,a1)
while l:
    print(l.val)
    l=l.next
                        
                    
