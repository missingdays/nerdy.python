#Euclidian algorithm
#Finds greatest common division
def gcd(a,b):

    while a!=0 and b!=0:

        if a > b:
            a = a % b

        else:
            b = b % a
            
    return a + b

print(gcd(20, 30)) #10
print(gcd(15, 30)) #15
print(gcd(480, 564)) #12
