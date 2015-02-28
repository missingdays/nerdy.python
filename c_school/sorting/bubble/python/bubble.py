A = [10, 2, 4, 5, 6, -3, 4, 0, 56]

i = len(A)
while i > 1:
   for k in xrange(i - 1):
       if A[k] > A[k + 1]:
           buf =  A[k]
           A[k] = A[k+1]
           A[k+1] = buf
   i -= 1


for i in range(len(A)):
    print(arr[i])
