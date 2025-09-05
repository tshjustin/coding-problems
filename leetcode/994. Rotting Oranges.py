from queue import Queue

# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         row = len(grid)
#         col = len(grid[0])

#         sol = [[float('inf') for _ in range(col)] for _ in range(row)]            
#         start_nodes = []
#         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#         for r in range(row): 
#             for c in range(col): 
#                 if grid[r][c] == 2:  
#                     sol[r][c] = 0
#                     start_nodes.append((r, c))

#                 elif grid[r][c] == 0:  
#                     sol[r][c] = -1  
                    
#                 elif grid[r][c] == 1:  
#                     sol[r][c] = float('inf') 

#         for start_x, start_y in start_nodes: 
#             q = Queue()
#             q.put((start_x, start_y)) 

#             while not q.empty(): 
#                 x, y = q.get()

#                 for dx, dy in directions: 
#                     new_x, new_y = x + dx, y + dy 
#                     if 0 <= new_x < row and 0 <= new_y < col:
#                         if grid[new_x][new_y] == 1 and sol[new_x][new_y] > sol[x][y] + 1:
#                             sol[new_x][new_y] = sol[x][y] + 1
#                             q.put((new_x, new_y))

#         res = 0
#         for r in range(row):
#             for c in range(col):
#                 if grid[r][c] == 1 and sol[r][c] == float('inf'):
#                     return -1  
#                 if sol[r][c] != -1:
#                     res = max(res, sol[r][c])
#         return res

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        """
        each node is can be "bracnhed" off 

        think of the update step as a level order traversal, once we go to the next level then we perform the update
     
        """

        row = len(grid)
        col = len(grid[0])

        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        fresh = 0 
        rotten = Queue() 

        for r in range(row): 
            for c in range(col): 
                if grid[r][c] == 2:  # if rotten 
                    rotten.put((r, c))
                
                elif grid[r][c] == 1: 
                    fresh += 1


        while not rotten.empty() and fresh > 0:
            minutes += 1 

            current_rotten = rotten.qsize() 

            for _ in range(current_rotten): 

                x, y = rotten.get()

                for dx, dy in directions: 
                    new_x, new_y = x + dx, y + dy
                    
                    # within bounds and not rotten 
                    # udpate to make it rotten 
                    if 0 <= new_x < row and 0 <= new_y < col and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2 

                        fresh -= 1 
                        rotten.put((new_x, new_y))

        return minutes if fresh == 0 else -1 
