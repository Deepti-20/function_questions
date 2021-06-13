
dic={1:"5",3:"6",7:"10",8:"4",5:"65"}
list=[]
list2=[]
for key in dic:
    list.append(key)
    list2.append(dic[key])
    d={}
    i=0
    while i<len(list2):
        d[list2[i]]=list[i]
        i+=1
print(d)