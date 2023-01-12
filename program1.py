#num = [10, 20, 30]
#num.append(40)
#num.insert(1, 60)
#print(num[-2])
#data = []
#data = reversed(num)
#print(list(data))
#num = [10, 20,25, 30, 40, 50]
#print(num[0:6:2])
# print(num[::4])
# print(num[-1:-4:-1])
#slicing
#std = [[20,30,40],[45,50,60]]
#print(sum(num))
#print(max(num))
#print(min(num))
#for n in std:
    #print(sum(n))
#i=[1,2,3,4,5,6,7,9]
#sum=0
#for num in i:
     #if(i.index(num)%2==0):
        # print(num*num)
         #sum=sum+(num**2)
         #print(sum)
#tuple
#tp=(1,2,3,4,)
#print(tp[2])
#print(tp[-1])
#tp[0]=100
#print(tp)

#dictionary
#d={'name':'shivv','sap id':52130505}
##print(d['name'])
#print(d.setdefault('contact',124578))
#print(d)
#for i in d.values():
    #print(i)
#for k,v in dic.items():
    #print({k,v})

#set
#a={1,2,3,4}
#b={5,6,7,8,4}
#print(a.union(b))
#print(a.intersection(b))
#print(b-a)

#cello copy
#l1=[1,2,3,4,5,6]
#l2=l1
#print(l1)
#l1.append(200)
#print(l1)
#print(l2)
#print(id(l1))
#print(id(l2))

#def square(n):
    #return n*n
#print(square(10))
#def getvalues(l):
    #return sum(l),max(l)
#num=[2,4,6,8]
#s,m = getvalues(num)
#print(s,m)

#def fact(n):
      #f=1
      #for i in range(1,n+1):
          #f=f*i
      #return f
#print(fact(6))

#def calculatewages(no,wages):
    #h=no*wages
    #return h
#print(calculatewages(100,20))


#def demo1(*n1):
    #print(n1)
#demo1(10,20,30)
#demo1(10)

#def demo2(**n1):
    #print(n1)
#demo2(name="shivv",num=100)

class Person:
    name=""
    id=0
    def __init__(self,name,id):
      self.name=name
      self.id=id
    def show (self):
        print(self.name,self.id)
p=Person("shivv",200)
p.show()










