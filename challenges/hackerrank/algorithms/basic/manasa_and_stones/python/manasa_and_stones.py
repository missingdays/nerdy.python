for i in range(int(input())):
    n = int(input())
    a = int(input())
    b = int(input())
    
    s = set()
    
    for j in range(n):
        su = 0
        for k in range(n-j-1):
            su += a
        for k in range(j):
            su += b
        s.add(su)    
        
    for elem in sorted(list(s)):
        print(elem, end=' ')
    print()    