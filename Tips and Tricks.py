
#List Comprehension making all lists o x,y,z that don't add up to 'n'
x, y, z, n = int(input()), int(input()), int(input()), int(input())
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

#list comprehension transform

i, j, k = int(input()), int(input()),int(input())
lst = []
for i in range(x):
    for j in range(y):
        for k in range(z):
            if i > j and j > k:
                lst.append([i,j,k])
print(lst)
#IS THE SAME AS below
lst_comprehend = [[i,j,k] for i in range(x) for j in range(y) for k in range(z) if i>j and j>k]
print(lst_comprehend)

#Getting a line of n numbers into a list:
list(map(int,input().strip().split()))
#Getting two integers:
n,m = input(),input()
#Getting a line of strings into a list:
list(input().strip().split())
#Getting a NumPy array with n rows as int:
import numpy as np
a = np.array(input().split(), int) for _ in range(n):