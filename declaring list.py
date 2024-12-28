list1=[2,3,4,2,3,4]
list1_uni=[]
list1_dup=[]
dict1={}
count=0
for i in list1:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i] +=1
for keys,val in dict1.items():
    print(f"{keys}apperaed of times {val} times")
