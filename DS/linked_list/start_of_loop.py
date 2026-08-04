class Solution:
    def cycleStart(self, head):
        fast=head
        slow=head
        while fast and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
            if(fast==slow):
                #loop detected
                fast=head
                while slow!=fast:
                    fast=fast.next
                    slow=slow.next
                return fast.data
        return -1
    