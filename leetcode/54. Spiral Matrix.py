class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        ## Recursive thinking 
        Another way to think about it is going layer by layer 

        After the first layer, there is the next layer, which is just a smaller matrix 

        Repeat the same processes for the next matrices that comes about

        ## Directions 
        direction = [right, down, left, up] => repeat 

        ## Boundaries 
        left_boundary +=1 
        right_boundary -=1 
        up_boundaary -=1 
        down_boundary +=1 
        if boundary collide => no more matrices => end the recusion 

        ## Implementation 
        left = 0 
        right = len(matrix[0]) + 1 # +1 such that its easier to code 
        up = 0
        down = len(matrix) +1 # easier to code 

        ## outputs 
        op = [1, 2, 3, 4]
        hit_right_boundary -> go down now
        decrement the top boundary (since we no longer need top row)

        go down until hit the bottom boundary -> go left now 
        decremenet right boundary (since we no longer need right col)

        go left until hit the left boundary -> go top now 
        decremenet bottom boundary -> (since we no longer need bottom row)
        
        go top until hit the NEW_TOP_BOUNDARY 
        incremenet left boundary -> (since we no longer need the left col)

        1. based on the trace above, we need to update our boundaries at all times 
        2. the boundaries would determine if we hit the base case 
        """

        result = []

        left_boundary, right_boundary = 0, len(matrix[0])
        top_boundary, bottom_boundary = 0, len(matrix) 

        print(bottom_boundary)
        
        # if any of the boundaries are equal, then we have converged 
        while left_boundary < right_boundary and top_boundary < bottom_boundary: 

            # get all the elements on the top row: 
            for i in range(left_boundary, right_boundary): 
                result.append(matrix[top_boundary][i]) # note top boudnary since we are brining the ceiling down, although intuitively should be row 

            # now we dont need the top row anymore, hence we can bring the ceiling down 
            top_boundary += 1

            if top_boundary >= bottom_boundary:
                break


            # get all the elements on the right row - later we'll discard the right row, so should be right boundary in the var 
            for i in range(top_boundary, bottom_boundary): 
                result.append(matrix[i][right_boundary-1]) # since we used len() previosuly for the ease, should do -1 for right and bottom 

            right_boundary -= 1
            
            if left_boundary >= right_boundary:
                break

            # get all the elements on the bottom row - later we'll discard the bottom row, bottom row should be in the var 
            for i in range(right_boundary-1, left_boundary-1, -1): 
                result.append(matrix[bottom_boundary-1][i])

            bottom_boundary -= 1
            
            if top_boundary >= bottom_boundary:
                break

            # finally going up -> discard the left col later
            for i in range(bottom_boundary-1, top_boundary-1, -1): 
                result.append(matrix[i][left_boundary])

            left_boundary += 1

        return result 
        
