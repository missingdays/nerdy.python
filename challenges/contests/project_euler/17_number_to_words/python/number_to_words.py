words = dict()
words[0] = "Zero"
words[1] = "One"
words[2] = "Two"
words[3] = "Three"
words[4] = "Four"
words[5] = "Five"
words[6] = "Six"
words[7] = "Seven"
words[8] = "Eight"
words[9] = "Nine"
words[10] = "Ten"
words[11] = "Eleven"
words[12] = "Twelve"
words[13] = "Thirteen"
words[14] = "Fourteen"
words[15] = "Fifteen"
words[16] = "Sixteen"
words[17] = "Seventeen"
words[18] = "Eighteen"
words[19] = "Nineteen"
words[20] = "Twenty"
words[30] = "Thirty"
words[40] = "Forty"
words[50] = "Fifty"
words[60] = "Sixty"
words[70] = "Seventy"
words[80] = "Eighty"
words[90] = "Ninety"
words[100] = "Hundred"
words[1000] = "Thousand"
words[10000] = "Million"
words[100000] = "Billion"
words[1000000] = "Trillion"
def getWord(n):
    string = ""
    if n >= 100:
        string = string + words[n//100] + " " + "Hundred"
        n = n % 100
    if n > 20 and string != "":
        string = string + " " + words[(n // 10) * 10]
        n = n % 10
    elif n > 20:
        string = string + words[(n // 10) * 10]
        n = n % 10
    if n > 0 and string != "":
        string = string + " " + words[n]
    elif n > 0:
        string = string + words[n]
    return string

for i in range(int(input())):
    string = ""
    n = int(input())
    if n >= 1000000000000:
        string = string + getWord(n//1000000000000) + " " + "Trillion"
        n = n % 1000000000000
    if n >= 1000000000 and string != "":
        string = string + " " + getWord(n//1000000000) + " " + "Billion"
        n = n % 1000000000
    elif n >= 1000000000:
        string = string + getWord(n//1000000000) + " " + "Billion"
        n = n % 1000000000
    if n >= 1000000 and string != "":
        string = string + " " + getWord(n//1000000) + " " + "Million"
        n = n % 1000000
    elif n >= 1000000:
        string =  string + getWord(n//1000000) + " " + "Million"
        n = n % 1000000

    if n >= 1000 and string != "":
        string = string + " " + getWord(n//1000) + " " + "Thousand"
        n = n % 1000
    elif n >= 1000:
        string = string + getWord(n//1000) + " " + "Thousand"
        n = n % 1000

    if n > 0 and string != "":
        string = string + " " + getWord(n)
    elif n > 0:
        string = string + getWord(n)
    elif n == 0:
        string = "Zero"
    print(string)
