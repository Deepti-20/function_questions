def sec_max(num):
	    i=0
	    max=0
	    while i<len(l):
	        if l[i]>max:
	            max=l[i]
	        i+=1
	        j=0
	        sec=0
	        while j<len(l):
	            if max>l[j]>sec:
	                sec=l[j]
	            j+=1
	    return sec
l=[50,40,210,23,70,57,12,5,10,7]
print(sec_max(l))