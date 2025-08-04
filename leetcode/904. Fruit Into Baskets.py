# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         """
#         we want the longest consecutive subarray of just consisting 2 numbers 

#         DP ? greedy ? 


#         Could just do a sliding window approach 

#         while array: 
#             keep track of the 2 elements we are currently seeing 

#             keep track of longest length

#             if we find new element, then we pop remove the element that is "away" from the current

#             1 2 2 0 

#             initally [1 ,2], once hit 0, then becomes [2, 0]

#         """
#     def totalFruit(self, fruits: List[int]) -> int:
#         max_length = 0
#         left = 0
#         cur = []
        
#         for right in range(len(fruits)):
            
#             # less than 2 fruits --> esnure 2 different fruits 
#             if len(cur) < 2 or fruits[right] in cur:
#                 if fruits[right] not in cur:
#                     cur.append(fruits[right])
            
#             # if another fruit, then shrink the left window until we get 1 distinct fruit 
#             else:
#                 while len(set(fruits[left:right])) > 1: # expensive operation 
#                     left += 1
#                 cur = [fruits[right-1], fruits[right]]
            
#             max_length = max(max_length, right - left + 1)
        
#         return max_length


from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        start = 0
        max_len = 0
        fruit_count = defaultdict(int)

        for end in range(len(fruits)):
            fruit_count[fruits[end]] += 1

            while len(fruit_count) > 2:
                fruit_count[fruits[start]] -= 1
                if fruit_count[fruits[start]] == 0:
                    del fruit_count[fruits[start]]
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len