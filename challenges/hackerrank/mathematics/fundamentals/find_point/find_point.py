for i in range(int(input())):
    ps = list(map(int, input().split()))
    
    diffs = [ps[2]-ps[0], ps[3]-ps[1]]
    
    print(ps[2] + diffs[0], ps[3] + diffs[1])
