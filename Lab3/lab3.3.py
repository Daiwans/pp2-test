#!/usr/bin/env python
# coding: utf-8

# In[ ]:
input_str = input()
A = input_str.split()
result = " ".join([A[i] for i in range(1, len(A)) if int(A[i]) > int(A[i - 1])])
print(result)
