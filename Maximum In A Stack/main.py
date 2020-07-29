# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#link of online compiler: https://www.programiz.com/python-programming/online-compiler/
class MaxStack:    
    def __init__(self):    
        self.data = []

    def push(self, val):    
        return self.data.append(val)
        

    def pop(self):    
        return self.data.pop()
        
    def max(self):    
        return max(self.data)    

s = MaxStack()    
s.push(1)    
s.push(2)    
s.push(3)    
s.push(2)    
print (s.max())    
# 3    
s.pop()    
s.pop()    
print (s.max())    
# 2