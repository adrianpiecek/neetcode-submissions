class MinStack:

    def __init__(self):
        self.size = 0
        self.stack = [None]
        self.mins = []


    def _resize(self,cap):
        buf = [None] * cap
        for i in range(self.size):
            buf[i] = self.stack[i]
        self.stack = buf     

    def push(self, val: int) -> None:
        if len(self.stack) == self.size + 1:
            self._resize(len(self.stack)*2)
        self.stack[self.size] = val

        if self.size > 0:
            if val <= self.mins[-1]:
                self.mins.append(val)
        else:
            self.mins.append(val)

        self.size += 1
        #print(self.stack)


    def pop(self) -> None:
        if self.mins and self.top() == self.mins[-1]:
            self.mins.pop()
 
        self.size -= 1
        #self.stack[self.size] = None
        if self.size <= len(self.stack)//4:
            self._resize(len(self.stack)//2)
        #print(self.stack)
            

    def top(self) -> int:
        return self.stack[self.size - 1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
        
