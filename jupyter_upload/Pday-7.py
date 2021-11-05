#!/usr/bin/env python
# coding: utf-8

# In[7]:


#class정의, class생성
#class 클래스명:
#클래스명() >> 생성자 >> instance (객체)

class Aclass:
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2
        print("class 생성")
        
    def __del__(self):
        print("class 소멸")
        
    def get_sum(self):
        print("class 내부 함수 실행")
        return (self.num1 + self.num2)
    
a = Aclass(10,20)
print(a.num1, a.num2, a.get_sum())
b = Aclass(30,40)
print(b.num1, b.num2, b.get_sum())


# In[ ]:




