class Stack():


    def __init__(self, size):

        #Array where we will store out values
        self.array_ = [0] * size

        #Size of current stack
        self.top = 0

    #Check whether stack is empty
    def isEmpty(self):

        return self.top == 0

    #Add new value to the end of stack
    def push(self, value):

        #Increment the size of the stack
        self.top = self.top + 1

        #Add value to the end of stack
        self.array_[self.top - 1] = value

    #Return last value that was pushed
    def pop(self):

        #If stack is not empty
        if(not self.isEmpty()):

            #Decrement the size of the stack
            self.top = self.top - 1

            #Return last value
            return self.array_[self.top]

#Create new stack
stack = Stack(6)

#Push some values
stack.push(5)
stack.push(6)
stack.push(0)

#Pop them back
print(stack.pop()) #0
print(stack.pop()) #6
print(stack.pop()) #5
