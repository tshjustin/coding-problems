class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Brute Force 
        -----------
        1. Create a new array 
        2. merge the 2 list 
        3. return the middle 


        2 pointer appraoch 
        ------------------
        observe that: 
        1. if we compare a[i] and b[j], if a[i] < b[j], then in the fully merged list, this would hold too 
        2. Hence if we move the pointer that is pointing to the smaller element, we are traversing the fully merged array correctly
        3. if we process half the elements (n/2 OR (n-1)/2), then that means we are at the median or close to it 
        
        
        binary search approach
        -----------------------
        """
        A, B = nums1, nums2

        total = len(A) + len(B)
        half = total // 2 

        # run BS on A, ensure that A is the smaller of the 2 arrays 
        if len(B) < len(A): 
            A, B = B, A

        l, r = 0, len(A) - 1

        while True: # garanteed a median 
            
            # middle value of the array A
            i = (l + r) // 2 

            # middle value of the array B --> -2 since 0 index for both arrays --> we want the index of the midpoint 
            j = half - i - 2 

            # now get the values that we want to compare with 
            # But note that could go OOB
            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i+1] if (i+1) < len(A) else float('inf') # gone too far to the right

            # same for B 
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if (j+1) < len(B) else float('inf')

            # correct partition 
            if Aleft <= Bright and Bleft <= Aright: 

                if total % 2: 
                    return min(Aright, Bright)

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 

            elif Aleft > Bright: 
                # too many elements from A, hence we shift the right pointer i - 1 --> reduce size of left partition 
                r = i - 1

            else: 
                l = i + 1





