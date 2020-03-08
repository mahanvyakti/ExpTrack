class myMath: 
    @staticmethod 
    def power(x,y): 
        ans = 1
        for i in range(y):
            ans = ans*x
        return ans
        #pass 


    @staticmethod 
    def fact(x):
        ans=1
        while x!=0:
            ans =  ans * x
            x = x-1
        return ans

class con1(myMath):
    def display(self, x):
        print(self.fact(x))

d = con1()
d.display(5)