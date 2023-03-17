# Write a program that asks a user for a number n and prints the sum of the numbers 
# from 1 to n
# <= input = 5
# => output = 15
x=int(input("Enter the number:"))
i=0
sum=0
while i<x:
    i+=1
    sum=i+sum
print(sum)
