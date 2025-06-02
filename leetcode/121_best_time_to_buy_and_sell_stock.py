class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Naive: 
        Loop through all combinations, return the max recorded -> O(n^2)

        Think of this heuristic: 


        If we keep a left and right pointer, what we want to achieve is that the left pointer 
        be some small value, while the right pointer is some large value 

        Hence if the right pointer hits some small value that is currently smaller than the current, we should 
        make the left pointer takes its place 

        else we just incrementally search 
        """
        sol = 0
        left = 0

        for right in range(1, len(prices)):
            
            # if its a potential profit - then we try for it 
            if prices[right] - prices[left] > 0: 
                sol = max(sol, prices[right] - prices[left])
                right +=1 

            # else its either a zero / negative profit, meaning that the right value is smaller, so we shift the left pointer to it 
            else: 
                left = right 

        return sol 

"""
Going through the solution, we actually implemented the following: 

if find a profit:
    check if the profit is greater than what we currently have 
    increment the window

if we find a loss: 
    shrink the window to its smallest 
    (WHY ?)
    Because we already found the profit of that window, hence any smaller subset of the window would not make more $
"""