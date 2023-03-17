# Given a list of strings, create two lists, the first one has the half of each string, the other 
# list contains the other half of the strings.
# <= input = ["apple"”","Maid"] 
# => output = [“app”,”Ma”] + [“le,”id”]
list4=['apple','Maid']
list5=[]
list6=[]
for n in list4:
    list5.append(n[0:len(n)//2])
    list6.append(n[len(n)//2:])
print(list5,list6)
