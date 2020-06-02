from time import time

m_counter=0
#complexity comparison counter

#merge function
def merge(l,au,low ,high,mid):
    global m_counter
    
    i=low
    j=mid+1
    k=low
    #k is moving from low to high for merging operation
    while( k <= high):
        m_counter+=1#comparison counter is taking track of the above
        if((i<=mid) and (j <= high)):
            if l[i] <= l[j]:
                au[k]=l[i]
                k=k+1
                i=i+1
            else:
                au[k]=l[j]
                k=k+1
                j=j+1
        elif(j <= high):
            au[k]=l[j]
            k=k+1
            j=j+1
        elif(i <= mid):
            au[k]=l[i]
            k=k+1
            i=i+1
        
        
    # copying the data from auxiliary array
    k=low
    while(k <= high):
        l[k]=au[k]
        k=k+1


    return



def merge_sort(l,au, low , high):
        #Merge sort recursion based
        if(low < high):
            mid=low + int((high-low)/2)
            merge_sort(l,au,low,mid)
            merge_sort(l,au,mid+1,high)
            merge(l,au,low,high,mid)

        return

if __name__=="__main__":
    
    filename="data1.1024"
    file_=open(filename,"r")
    lines=file_.readlines()
    data=[]
    aux_=[]
    for line in lines:
        line=line.strip()
        data.append(int(line))
        aux_.append(0)
    t0 = time()    
    merge_sort(data,aux_,0,len(data)-1)
    t1 = time()
    print("The complexity counter for the top down merge sort for data set of size ",len(data),"is : ",m_counter)
    print("The time taken :",(t1-t0)*1000," ms")
    print("The Sorted Data is as follows :")
    print(data)



