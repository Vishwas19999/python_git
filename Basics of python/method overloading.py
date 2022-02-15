# class calculate:
#     def sub(self,a,b):
#         print("a-b={}".format(a-b))
#
#     def sub(self,a,b,c):
#         print("a-b-c={}".format(a-b-c))
#
# c1=calculate()
# c1.sub(10,8,6)
# c1.sub(5,3)

#using default arguments
class calculate:
    def sub(self,a,b,c=0):
        if c>0:
            print("a-b-c={}".format(a-b-c))
        else:
            print("a-b={}".format(a-b))

c1=calculate()
c1.sub(10,8,6)
c1.sub(6,3)

#using variable len arg
class calculate:
    def add(self,*args):
        res=0
        for param in args:
            res+=param
            print("res:{}".format(res))

c1=calculate()
c1.add(10,4,6)
c1.add(4,2)