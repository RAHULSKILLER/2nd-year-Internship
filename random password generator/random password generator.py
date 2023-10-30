#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import string

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate and print a random 8-character password
password = generate_random_password()
print(password)


# In[11]:


import random

def generate_password(length):
    "This function accepts a parameter 'length' and returns a randomly generated password"
  
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
    pass_str = ""
  
    for i in range(length):
        pass_str = pass_str + random.choice(list_of_chars)
      
    return pass_str

if __name__ == "__main":
    length = int(input("enter the length of password")
    pass_str = generate_password(length)
    print("A randomly generated Password is:", pass_str)


# In[1]:


import random

def random_password(length):
    
  
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
    new_list= ""
  
    for i in range(length):
        new_list = new_list + random.choice(list_of_chars)
      
    return new_list


length = int(input("enter length of password")) 
new_list = random_password(length)
print("A randomly generated Password is:", new_list)


# In[2]:


import random

def random_password(length):
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    special_chars = "!@#$%^&*()_-+="
    new_list = []

    if length >= 6:
        
        special_char_position = random.randint(0, length - 1)
        for i in range(length):
            if i == special_char_position:
                new_list.append(random.choice(special_chars))
            else:
                new_list.append(random.choice(list_of_chars))
    else:
        for i in range(length):
            new_list.append(random.choice(list_of_chars))

    return ''.join(new_list)

length = int(input("Enter the length of the password: "))
new_list = random_password(length)
print("A randomly generated Password is:", new_list)


# In[ ]:





# In[ ]:




