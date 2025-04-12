class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """

        Multisource BFS 

        Enqueu all the possible starting positions 

        for each node :
            perfrom BFS 
            update the shortest path iff the path to get to it is shorter than the current + 1

        Note that the shortest path from non-0 to 0 is the same for 0 to non-0
        """
        from queue import Queue
        
        if not mat:
            return []
            
        rows, cols = len(mat), len(mat[0])
        result = [[float('inf')] * cols for _ in range(rows)]
        q = Queue()
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    result[r][c] = 0
                    q.put((r, c))

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while not q.empty():
            r, c = q.get()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check if in bounds and if we found a shorter path
                if (0 <= nr < rows and 0 <= nc < cols and result[nr][nc] > result[r][c] + 1):
                    result[nr][nc] = result[r][c] + 1
                    q.put((nr, nc))
        
        return result