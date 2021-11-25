
from collections import Counter

num_of_shoes = int(input()) #X number of shoes
shoe_list = Counter(map(int,input().split())) #list of shoe sizes
num_of_customer = int(input()) #N number of customers

income = 0

for i in range(num_of_customer):
    size,price = map(int,input().split()) #getting the input for size and price
    if shoe_list[size]:
        income += price
        shoe_list[size] -= 1
print(income)

x = "1 2 3   4"
x.split()
print(x)