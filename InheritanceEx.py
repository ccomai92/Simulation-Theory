class A(object): 
    i = 4
    def write(self): 
        print("In A:" + str(A.i))
   
        
# import myclasses
# class B(myclasses.A)     
# from myclasses import A 
# class B(A)
class B(A): 
     def write(self):
         super(B, self).write() 
         print("In B: " + str(B.i*2)) 
         
class C(A): 
    def write(self): 
        super(self.__class__, self).write() 
        
a = A()
b = B()
c = C() 
a.write()
b.write() 
c.write() 
