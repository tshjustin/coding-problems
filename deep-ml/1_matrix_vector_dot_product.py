def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    """
    [1, 2] @   [1, 2] 
    [3, 4]     [3, 4]

    For each row of A: 
        dot product for each for of B 

    [1*1 + 2*3, 1*2 + 2*4]
    [3*1 + 4*3, 3*2 + 3*4]
    """
    # check if col of A match with row of B 
    if len(a[0]) != len(b):
        return - 1

    result = []

    # for each row of a 
    for i in range(len(a)):
        total = 0

        # multiply for each element of b 
        for k in range(len(b)):
            total += a[i][k] * b[k]
        result.append(total)

    return result