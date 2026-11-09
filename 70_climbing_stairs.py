class Solution:
    def climbStairs(self, n: int) -> int:
        if n==2:
            return 2

        first=0
        second=1
        curr=0
        for i in range(0,n):
            curr=first+second
            first=second
            second=curr
        
        return curr