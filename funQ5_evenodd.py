# Q5. part-2
def check_num_list(list1,list2):
    i=0
    while i<len(list1):
        j=0
        while j<len(list2):
            if list1[i]%2==0 and list2[j]%2==0:           
                print(list1[i],list2[j],"even number")
            else:
                print(list1[i],list2[j],"not even number")
            j=j+1
            i=i+1
list1=[2, 6, 18, 10, 3, 75]
list2=[6, 19, 24, 12, 3, 87]
check_num_list(list1,list2)

# check in list same index numbers are even or odd.