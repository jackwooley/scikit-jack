def matmul(A, B):
    """Multiply A and B together.
    
    Params:
    :A, B -- need to both be either numpy arrays or lists of lists, with the appropriate dimensions.
    Can scalars, but need to be formatted as list of list of length 1.
    """

    # check dimensions to make sure they're compatible
    if len(A[0]) != len(B):
        raise ValueError('The shapes of your matrices are incompatible!\n'
                        f'A: {len(A)} x {len(A[0])}\n'
                        f'B: {len(B)} x {len(B[0])}\n')
    
    # to make indexing more easy, let's transpose B
    B_T = T(B)

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


def T(A):
    """Transpose a matrix A.
    
    Params:
    :A -- either numpy array or list of lists, with each interior list having the same length.
    Can handle scalars, but need to be formatted as list of list of length 1.
    """

    # check dimensions to make sure they're compatible
    baseline = len(A[0])
    lengths = [1 if len(i) == baseline else 0 for i in A]
    if sum(lengths) != sum([1 for _ in A]):
        raise ValueError('Are all the rows of your matrix the same shape?')
    
    # initialize empty matrix of correct dimensions so we can add stuff at the right indices
    A_T = []
    for i in range(len(A[0])):
        A_T.append([0] * len(A))

    # swapping the i,j positions to j,i
    for i in range(len(A)):
        for j in range(len(A[0])):
            A_T[j][i] = A[i][j]
    
    return A_T
