nums = []

def getLast(first, second, third):
    s = []
    first = str(first)
    second = str(second)
    third = str(third)

    numbers = [third, second, first]
    for number in numbers:
        c = 0
        while c < len(number) and len(s) < 10:
            s.append(number[c])
            c = c + 1

    return ''.join(s)

def mutalize(num):
    s = str(num)
    return num * pow(10,(5-len(s)))

def prep(s):
    l = list(str(s))
    while len(l) < 5:
        l.insert(0,'0')
    return ''.join(l)

n = int(input())
nums = []
for i in range(n):

    s = input()
    temp = []
    for k in range(0, 50, 5):
        num = s[len(s)-k-5:len(s)-k]
        temp.append(num)

    nums.append(list(map(int,temp)))
buf = 0
answ = []
for k in range(10):
    su = buf
    for i in range(len(nums)):
        su += nums[i][k]
    buf = su // 100000
    answ.append(su % 100000)
while buf > 0:
    if buf // 100000 == 0:
        answ.append(buf)
        buf = 0
    else:
        answ.append(mutalize(buf % 100000))
        buf = answ[len(answ)-1] // 100000
for i in range(len(answ)):
    if answ[i] < 10000 and i!=len(answ)-1:
        answ[i] = prep(answ[i])
a = len(answ) - 1
print(int(getLast(answ[a-2], answ[a-1], answ[a])))
