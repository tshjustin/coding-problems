# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = left + (right - left) // 2
            
            # if middle bad, then first bad should either be mid or comes before it 
            if isBadVersion(mid):
                right = mid

            # update step 
            else:
                left = mid + 1
        
        # terminate when the pointers converge to the first bad 
        return right