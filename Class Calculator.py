class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print('add of a and b is = ',self.a+self.b)
    def mul(self):
        print('mul of a and b is = ', self.a*self.b)
    def div(self):
        print('div of a and b is = ', self.a/self.b)
    def sub(self):
        print('sub of a and b is = ', self.a-self.b)

obj=cal(10,25)
obj.add()
obj.mul()
obj.div()
obj.sub()
