from Number import Number
import numpy as np

a = Number(1)
b = Number(2)

A = np.array([[Number(1),  Number(2)]], dtype=Number)
print(A)
B = np.array([[Number(3)],  [Number(5)]], dtype=Number)
print(B)
print(A@B)
print(Number.ADD_counter, Number.MUL_counter)
print((B@A))
print(Number.ADD_counter, Number.MUL_counter)