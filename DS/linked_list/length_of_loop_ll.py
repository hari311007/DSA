class Solution:
    def lengthOfLoop(self, head):
        fast=head
        slow=head
        while fast and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                #loop found
                temp=slow.next
                count=1
                while temp is not slow:
                    count+=1
                    temp=temp.next
                return count
        return 0
        