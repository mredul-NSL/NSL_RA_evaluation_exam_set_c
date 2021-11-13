import numpy as np

A = np.array(
    [[ 0,  1,  2,  3],
[ 4,  5,  6,  7],
[ 8,  9, 10, 11],
[12, 13, 14, 15]]
)

print("The answer of a: \n",A[1:3, 1:3])

print("The answer of b:\n", A[:, 0:3])

print("The answer of c:\n", A[1:, :])