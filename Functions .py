#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Functions 
 #for the cutom requirement we can write and design  our own functions 
    #understanding zen of python 
import this 


# In[9]:


#def is the keyword for defining the  functions 
#for giving the function name we have to use lower case only
  
#req: Create a greett fuction

def greet():    #degining / declaring the functions 
    """creating  a greet funtion"""
    #doc string ===>commenting indside function 
    print("Hello")
    greet() #function call 
    
    
    
    


# In[41]:


# req: create a fun to greet the user that we are passing to  the function 
def greetuser(username):  # parameter passing during the fucntion declaratiion 
    print(f"Hello,{username.title()}")
greetuser('athira')  # It is called as argument Passing"
greetuser('anoop')   


# In[40]:


def greetuser(username): 
    print(f"Hello,{username.title()}")
greetuser('athira')  
greetuser('Reji'.title())   


# In[56]:


#type of arguments
# req: create a describe pet function  where it takes 2 parameters
#1. animal type 2. petname 

def describe_pet(animaltype,petname):
    print(f"I have a{animaltype}")
    print(f"my{animaltype}'sname is'{petname}")
describe_pet('dog', 'rex')
describe_pet('cat', 'reji')
describe_pet('abi', 'fish')


# In[58]:


#by default functions will be having the positional arguments..............!
describe_pet(petname='abi', animaltype='fish')


# In[60]:


# keyword argmuments 
#req: animaltype ->>>assumed to the dog
#interview questions 
# where declare the default arguments ? it declare the end , not in begnining 
def describe_pet(animaltype,petname='dog'):
    print(f"I have a{animaltype}")
    print(f"my{animaltype}'sname is'{petname}")
describe_pet('burno')
describe_pet('teenu', 'rabbit')


# In[59]:


def describe_pet(animaltype='dog',petname):
    print(f"I have a{animaltype}")
    print(f"my{animaltype}'sname is'{petname}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




