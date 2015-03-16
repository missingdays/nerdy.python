'''
    type: algorithm
    theme: math
    sub-theme: calculate
    name: Least common multiply
    author of code: Evgeny @missingdays Bovykin

'''

#Finds least common multiply
def lcm(a, b):
    return a * b / gcd(a, b)

#Finds greatest common division
def gcd(a, b):
    while a!=0 and b!=0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

print(lcm(20, 30)) #60
print(lcm(17, 9)) #153
