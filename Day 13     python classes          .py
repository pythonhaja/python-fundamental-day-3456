#!/usr/bin/env python
# coding: utf-8

# In[13]:


class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def jump(self):
        print(f"{self.name} is now jumping on the command")
    def rollover(self):
        print(f"{self.name} is now rolling over on the command")
    def eat(self):
        print(f"{self.name} is now eating")
    def sleep(self):
        print(f"{self.name} is now sleeping")
    def details(self):
        print(f"my dog name is {self.name}")
        print(f"{self.name}is of {self.age}years old")

test=dog('rex',2)
test.jump()
test.rollover()
test.eat()
test.sleep()
test.details()

    


# In[ ]:





# In[12]:


class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def jump(self):
        print(f"{self.name} is now jumping on the command")
    
    def rollover(self):
        print(f"{self.name} is now rolling over the command")
    
    def eat(self):
        print(f"{self.name} is now eating")
    
    def sleep(self):
        print(f"{self.name} is now sleeping")
   
    def details(self):
        print(f"My dog name is {self.name}")
        print(f"{self.name} is of {self.age} years old")
              
test=Dog('rex',2)
test.jump()
test.rollover()
test.eat()
test.sleep()
test.details()


# In[ ]:





# In[ ]:





# In[ ]:




