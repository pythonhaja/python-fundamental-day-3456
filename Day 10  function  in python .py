#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Def is the keyword for definig the functions
#for  giving the functions name we have to use small case letter only 


# In[10]:


#req: Create a greet function
def greet(): #defining /declaring function
    """creating a greet function """  # commenting inside function 
    print("Hello")
greet()
    


# In[8]:


# req: create a fun to Greet the user that we are passing to the functions 

def greetuser(username):
    print(f"Hello,{username.title()}")
        
greetuser('keerthika')
greetuser('Anup')
        


# In[ ]:


# req create a describe pet function where it takes two parameters belows:
#1.ANIMAL TYPE 2. PET NAME 


# In[11]:


def describe_pet(animaltype,petname):
    print(f"I have a {animaltype}")
    print(f"my{animaltype}'s name is {petname}")
    
describe_pet('dog','rex')
describe_pet('cat','fari')
describe_pet('goldy','fish')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




