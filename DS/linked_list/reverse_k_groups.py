class Solution:
    def reverseKGroup(self, head, k):
        #curr,prev,temp,prevtail,grouphead,newhead
        curr=head
        prevtail=None
        newhead=None
        while curr is not None:
            grouphead=curr
            prev=None
            count=0
            while curr and count<k:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
                count+=1
            if newhead is None:
                newhead=prev
            if prevtail:
                prevtail.next=prev
            prevtail=grouphead
        return newhead