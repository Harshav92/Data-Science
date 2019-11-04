#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


games = int (input("enter the num of games you would like to play "))


# In[4]:


for i in range(1 , games+1) :
    num = random.randint(1 , 25)
    print("game number" , i)
    guess = int(input (" guess the number between 1 and 25"))
    if guess == num :
        print("your guess is right")
    else :
        if guess > 25:
            print (" you selected a number above 25")
        elif (guess < 1) :
            print ("you selected a number below 1 ")
        else :
            print ("you guess is wrong")
    
    

