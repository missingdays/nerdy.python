'''
    type: algorithm
    theme: arrays
    sub-theme: sorting
    name: selection sorting
    author of code: Evgeny @missingdays Bovykin

'''

A = [10, 2, 4, 5, 6, -3, 4, 0, 56]

for i in range(len(A)):
    minimum = i
    for k in range(i, len(A)):
        if(A[k] < A[minimum]):
            minimum = k

    buf = A[i]
    A[i] = A[minimum]
    A[minimum] = buf

for i in range(len(A)):
    print(A[i])
