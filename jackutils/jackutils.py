def matmul(A, B):
    """Multiply A and B together.
    
    Params:
    :A, B -- need to both be either numpy arrays or lists of lists, with the appropriate dimensions.
    Can scalars, but need to be formatted as 
    """

    # check dimensions to make sure they're compatible
    if len(A[0]) != len(B):
        raise ValueError('The shapes of your matrices are incompatible!\n'
                        f'A: {len(A)} x {len(A[0])}\n'
                        f'B: {len(B)} x {len(B[0])}\n')
    
    # to make indexing more easy, let's transpose B
    # initialize empty matrix of correct dimensions so we can add stuff at the right indices
    B_T = []
    for i in range(len(B[0])):
        B_T.append([0] * len(B))

    # swapping the i,j positions to j,i
    for i in range(len(B)):
        for j in range(len(B[0])):
            B_T[j][i] = B[i][j]

    # initialize array of 0s to fill
    result = []
    for i in range(len(A)):
        result.append([0] * len(B[0]))

    for i in range(len(A)):
        for j in range(len(B_T)):
            element = 0
            for k in range(len(A[0])):
                if len(A[0]) == len(B_T[0]):
                    element += A[i][k] * B_T[j][k]
                result[i][j] = element

    return result
