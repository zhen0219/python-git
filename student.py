                                                                                                                                                           15,9          All
#!/usr/bin/env python
#-*- coding:utf-8 -*-

'student class'
__author__='Zhen'

import sys
import os

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%d'%(self.name,self.score))
    def get_grade(self):
        if(self.score>90):
            print('Great! You got A!')
        elif(self.score>75):
            print('B!')
        else:
            print('Work better next time! C!')


if __name__=='__main__':
    a=Student('Alice',99)
    b=Student('Bob',88)
    c=Student('Simon',66)
    a.print_score()
    a.get_grade()
    b.print_score()
    b.get_grade()
    c.print_score()
    c.get_grade()
    
    
  
  
  
  
  
  
  
#!/usr/bin/env python
#-*- coding:utf-8 -*-

'student class'
__author__='Zhen'

import sys
import os

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%d'%(self.name,self.score))
    def get_grade(self):
        if(self.score>90):
            print('Great! You got A!')
        elif(self.score>75):
            print('B!')
        else:
            print('Work better next time! C!')


if __name__=='__main__':
    a=Student('Alice',99)
    b=Student('Bob',88)
    c=Student('Simon',66)
    a.print_score()
    a.get_grade()
    b.print_score()
    b.get_grade()
    c.print_score()
    c.get_grade()

    
    
    
    #!/usr/bin/env python
#-*- coding:utf-8 -*-

'a test module'

__author__='Alice Zhen'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello World')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
    
    
    
    
