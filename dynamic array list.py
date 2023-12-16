import ctypes

class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0
        #create C type array with size = self.size
        self.A = self.__make_array(self.size)
       
    def __len__(self):
        return self.n
    
    # PRINT LIST IN []
    def __str__(self):
        #[1,2,3,4]
        result = ''
        for i in  range(self.n):
            result = result + str(self.A[i])+ ","
        return '[' + result[:-1] + ']'
   
    #INDEXING
    def __getitem__(self,index):
        if 0<= index <self.n:
          return self.A[index]
        else:
            return 'IndexError = Index out of range'


    def append(self,item):
        if self.n == self.size:
            #resize
            self.__resize(self.size*2)
        
        #append
        self.A[self.n] = item
        self.n = self.n +1

    #POP ITEM FROM LIST
    def pop(self):
        if self.n == 0 :
            return("empty list")
        print(self.A[self.n-1])
        self.n = self.n-1

    # Clear
    def clear(self):
        self.n=0
        self.size=1

    # Find
    def find(self,item):
        for i in range(self.n):
         if self.A[i] == item:
            return i 
        return "Value error" 

    #INSERT
    def insert(self,pos ,item):
        if self.n == self.size:
            self.resize(self.size*2)
        for i in range(self.n,pos , -1):
            self.A[i]= self.A[i-1]
        self.A[pos] = item
        self.n = self.n + 1
        
    # DELETE
    def __delitem__(self,pos):
        if 0<= pos <self.n:
            for i in range(pos,self.n-1):
             self.A[i]= self.A[i+1]
            self.n = self.n - 1 

    # Remove
    def remove(self,item):
        pos = self.find(item)
        
        if type(pos)==int:
            #delete
            self.__delitem__(pos)
        else:
            return pos

    def __resize(self,new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity

        # copy the content of A to B  
        for i in range(self.n):
            B[i]= self.A[i]

        #ressign A
        self.A = B
    def __make_array(self,capacity):
        # create a C type array(static and referential array) with size capacity
        return(capacity* ctypes.py_object)()

L = MeraList()
L.append(1)
L.append(2) 
L.append(3)
L.append(5)
L.append(4)
L.append("hello")
L.append(True)
print(L)
# L.insert(3,0)
# print(L)
# del L[1]
# print(L)
# L.remove(10)
# print(L)


# some assignment on dynamic array.
"""
sort /min/max/sum
extend
negative indexing
slicing
Merge.
"""