#!/usr/bin/env python
# coding: utf-8

# In[ ]:


input_str = input()
A = input_str.split()
result = " ".join([x for x in A if int(x) % 2 == 0])
print(result)


# In[ ]:




