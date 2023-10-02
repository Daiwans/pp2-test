#!/usr/bin/env python
# coding: utf-8

# In[ ]:
input_str = input()
A = input_str.split()
maxvalue = max(A)
maxindex = A.index(maxvalue)
print(maxvalue, maxindex)
