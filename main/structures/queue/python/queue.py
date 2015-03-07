class Queue():


    def __init__(self, size):

        #Array where we will store out values
        self.array_ = [0] * size

        #Pointer to the beginning of queue
        self.head = 0

        #Pointer to the end of queue
        self.tail = 0

    #Add new value to queue
    def enqueue(self, x):

        #Add value to the end of queue
        self.array_[self.tail] = x

        #If tail points to the end of the array
        if(self.tail == len(self.array_) - 1):

            #Point tail to the beginning of the array
            self.tail = 0

        else:

            #Increment tail
            self.tail = self.tail + 1

    #Get first value from queue
    def dequeue(self):

        #Store this value to x
        x = self.array_[self.head]

        #If head points to the end of the array
        if(self.head == len(self.array_) - 1):

            #Point head to the beginning of the array
            self.head = 0

        else:

            #Increment head
            self.head = self.head + 1

        #Return value
        return x

#Create new queue
queue = Queue(3)

#Add some values to it
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(1)

#Get values
print(queue.dequeue()) #4
print(queue.dequeue()) #5
print(queue.dequeue()) #1
