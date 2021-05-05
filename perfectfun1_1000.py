# perfect numbers 1 to 1000 in function :
def perfect_num():
    num=1
    while num<1000:
        sum=0
        i=1
        while i<num:
            if num%i==0:
                sum=sum+i
            i=i+1
        if sum==num:
            print(num,"perfect")
        else:
            print(num,"not perfect")
        num+=1
perfect_num()