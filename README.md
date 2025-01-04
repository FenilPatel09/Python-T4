class Father:
    
    def __init__(self,m):
        self.money=m
        print("Father constructor")
        
    def show(self):
        print("Father method")
        
class Son(Father):
    
    def __init__(self,m):
        print("Son constructor")
        # super().__init__(m)
        Father.__init__(self,m)
    
    def disp(self):
        print("Son method ",self.money)
        
s=Son(5000)
s.show()
s.disp()
