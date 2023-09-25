#!/usr/bin/env python
# coding: utf-8

# In[2]:


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
color1 = (x1 + y1) % 2
color2 = (x2 + y2) % 2
if color1 == color2:
    print("YES")
else:
    print("NO")

