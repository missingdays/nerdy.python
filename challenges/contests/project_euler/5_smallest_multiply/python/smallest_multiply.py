n = int(input())

def calc(array):
    mult = 1
    new_array = []
    for i in range(len(array)-1, -1, -1):
        if mult % array[i] != 0:
            mult = mult * array[i]
            new_array.append(array[i])
    return new_array

def list_mult(array):
    mult = 1
    for i in range(len(array)):
        mult = mult * array[i]

    return mult

for i in range(n):

    num_list = []
    mult = 1

    for i in range(1, int(input())+1):
        if mult % i != 0:
            num_list.append(i)
            num_list = calc(num_list)
            mult = list_mult(num_list)

    print(mult)
