class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Each number has a choice of being chosen or not 

        current num = 1 
        [] [1]

        current num = 2

        [] -> [], [2]
        [1] -> [1], [1, 2]

        current num = 3

        [] -> [], [3]
        [2] -> [2], [2, 3]
        [1] -> [1], [1, 3]
        [1, 2] -> [1, 2], [1, 2, 3]

        Gathering all the solutions 
        [], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]


        One way we can mimic choosing or not choosing the current value is by doing a +1

        in the most simple case, just think of the very top level
        """
        res = []

        def dfs(index, current): 
            """ 
            index = current index of the nums we are considering 

            current = currently the subset that we are considering --> in the below implementation , we would go to [1, 2, 3] first 
            """
            if index == len(nums):
                res.append(current.copy())
                return 
            
            # we choose to take the element
            current.append(nums[index])
            dfs(index+1, current)

            # once we have reached the end [1, 2, 3], we would then call the function again
            # but since index == len(nums), we perform the copy [1, 2, 3] to the result array 
            # then we return 
            # now note that we have current = [1, 2, 3], hence we need to pop out the last element
            current.pop()

            # now we explore the next branch (left branch that should yield the result [1, 2])
            dfs(index+1, current)
            return

        dfs(0, [])
        return res 

"""
yay first recursion solved i guess 

1. Draw out decision tree 

2. Explore the choice of taking and not taking --> see how it manifest [append + pop after]

3. Note that res can be invoked inside the function call, hence res is treated as some global variable 

4. Key observation is that we explore until [1, 2, 3] first.

5. Now note that the next call after pop dfs(index+1, current) ==> dfs(2, [1, 2]) => hence we would not pick the item=3,
since we dont even have it appended to our array ! ==> this mimics skipping that value 


"""