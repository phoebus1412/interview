outputs for the following codes
1,class Parent(object)
      x=1
  class Child1(Parent)
      pass
  class Child2(object)
      pass

  print Parent.x,Child1.x,Child2.x
  Child1.x=2  
  print Parent.x,Child1.x,Child2.x
  Parent.x=3
  print Parent.x,Child1.x,Child2.x

2,def div1(x,y):
      print("%s/%s=%s" % (x,y,x/y))
  def div2(x,y):
      print("%s//%s=%s" % (x,y,x//y))	
  div1(5,2)
  div1(5.,2)
  div2(5,2)
  div2(5.,2)

3,list=['a','b','c','d','e']
  print list[10:] 

4,def multipliers():
      return [lamdba x:i*x for i in range(4)]
  print [m(2) for m in multipliers()]

5,def extendlist(val,list=[]):
	list.append(val)
	return list
list1=extendlist(10)
list2=extendlist(123,[])
list3=extendlist('a')

print "list1=%s" % list1
print "list2=%s" % list2
print "list3=%s" % list3
 
Answers:
1.	1,1,1
	1,2,1
	3,2,3
	Atributes of a class in python are viewed as dictionary.

2.      In python 3:
	2.5,2.5,2,2.0
	In python 2:
	2,2.5,2,2.0
	If you want to get the same result in python 3,try: from __future__ import division. And "//" will always be exact division.

3.      []
        if you print list[10],it will result in IndexError
	if you print list[10:],it will return an empty list.(which is annoying)

4.      [6,6,6,6]	
        solutions:
	1. return[lamdba x,i=i:i*x for i in range(4)]	
        2. from functools import partial
	   from operator import mul
	   def multipliers():
	       return[partial(mul,i) for i in range(4)]

5.      list1=[10,'a']
        list2=[123]
	list3=[10,'a']
	if you are expecting:
		list1=[10]
		list2=[123]
		list3=['a']
	try the following:
		def extendlist(val,list=None):
			if list is None:
				list=[]
			list.append(val)
			return list

