'''
    type: algorithm
    theme: string
    sub-theme: search sub string
    name: Knuth-Morris-Pratt
    author of code: Evgeny @missingdays Bovykin

'''


def substring_index(origin, sub):

    i_origin = 0 # current character in origin
    i_sub = 0 # in sub

    failed = [None] * len(sub)

    failed[0] = -1

    for i in range(1, len(sub)):
        temp = failed[i-1]
        while temp > -1 and sub[temp] != sub[i-1]:
            temp = failed[temp]
        failed[i] = temp + 1    

    while i_origin < len(origin) and i_sub < len(sub):
        if i_sub == -1 or origin[i_origin] == sub[i_sub]:
            i_origin += 1
            i_sub += 1
        else:
            i_sub = failed[i_sub]

    if i_sub > len(sub) - 1:
        return i_origin-len(sub)
    else:
        return -1
