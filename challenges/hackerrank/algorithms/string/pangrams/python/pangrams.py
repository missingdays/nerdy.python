
#Get string as lowercase
s = input().lower()

#List where we will store letters
letters = []

#For every character in input string
for c in s:

    #If this characted is not presented in letters list yet
    if not c in letters:

        #Append it to the list
        letters.append(c)

#If every character is presented
if(len(letters) == 27):

    #This is a pangram!
    print("pangram")

#Else
else:

    #It's not!
    print("not pangram")
