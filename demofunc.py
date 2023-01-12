#def add(x,y):
    #return x+y
#a=add
#print(a(10,40))

#def incr(x):
    #return x+1
#def decr(x):
    #return x-1
#def operator(func,n):
    #r=func(n)
    #return r
#print(operator(decr,10))

#def even(x):
    #for i in range(x):
       #if  (i%2==0):
           #return i
#def odd(y):
    #for i in range(y):
       #if  (i%2!=0):
           #return i
#def operator(func,n):
    #r=func(n)
    #return r
#print(operator(even,10))
#print(operator(odd,20))

#closure
#def function1(txt):
    #def functiion2():
       #print(txt)
    #return function2
#msg=functional("hello")
#del function2()
    #msg()

def add_num(n):
    def add(x):
        return x+n
    return add
num1=add_num(10)
num2=add_num(12)
print(num1(5))
print(num2(5))

#decorators

#def function1(fun)
    #def function2():
        #print("hi from function 2")
        #func()
    #return function2
#@function1
#def demo():
 #print("how are you"):
#f=function1(demo)
#f()
#demo()




