class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        All the 1s are starting point and we can start a bfs 

        once visited, then turn that area == 0 to mark it as visisted

        once visiting until no more neighbours, then increment sol by 1 

        start with new starting point
        """

        from queue import Queue 

        sol = 0 
        row = len(grid)
        col = len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(row): 
            for c in range(col): 

                q = Queue() 

                if grid[r][c] == "1": 
                    q.put((r, c))
                    grid[r][c] = "0" # small optim since it cold be visied again 

                    while not q.empty():
 
                        x, y = q.get()

                        for dx, dy in directions: 
                            new_x, new_y = x + dx, y + dy 

                            if 0 <= new_x < row and 0 <= new_y < col and grid[new_x][new_y] == "1": 
                                q.put((new_x, new_y))
                                grid[new_x][new_y] = "0"

                    sol += 1
        return sol 

        