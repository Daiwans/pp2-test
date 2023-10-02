#!/usr/bin/env python
# coding: utf-8
# In[ ]:
input_str = input()
A = input_str.split()
for i in range(1, len(A)):
if int(A[i]) * int(A[i - 1]) > 0:
print(A[i - 1], A[i])
break
