#!/usr/bin/env python
# coding: utf-8

# In[7]:


students=('Anoop','RAVI','Namitha','arshitha','keerthi')
print(students)
for x in students:
    print(x)


# In[3]:


students=('Anoop','RAVI','Namitha','arshitha','keerthi')
student.append('Prakash')


# In[5]:


Dimensions =(200,50)
print(Dimensions)
Dimensions[0]=250


# In[6]:


Dimensions =(200,50)
print(Dimensions)


# In[15]:


# Dictionaries 


alien={'color':'green','points':5}
print(alien)
print(alien['color'])
print(alien['points'])


alien['Starting_point']=15
alien['Current_position']=10
print(alien)

# modify dic
alien['color']='yellow'
alien['points']=10
print(alien)


# In[20]:


# Create a facebook account

Useraccount = {'username':'code training academy','last name':'academy','dot':'01-01-2019','pwd':'5321'}
print(Useraccount )
Useraccount['Location']='faizilcafe'
print(Useraccount )
print(alien)
del alien['Starting_point']


# In[49]:


# for loop implementation of dictionary 

for k,v in alien.items():
    print(k)
    print(v)
    
    # other loop 
for a,b in Useraccount.items():
    print(a)
    print(b)
    
#enhancement of code 
 for a,b in Useraccount():
    print(f"key:{a}")
       print(f"value:{b}.\n")

    
    


# In[47]:


for a,b in Useraccount.items():
   print(f" key:{a}")
   print(f" value:{b}.\n")


# In[50]:



for a in Useraccount.keys():
    print(f"key:{a}")


# In[52]:



for b in Useraccount.values():
    print(f"values:{b}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




