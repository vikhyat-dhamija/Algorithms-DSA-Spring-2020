from time import time
m_counter=0
#complexity comparison counter

#merge function
#This merge is different in parameters function is same as the one did in top down
#list , auxiliary array , low , high indexes , size depending on the iteration of merging i.e. 2 , 4 etc. are being passed
def merge(list_,au,l,ls,h,size):
    global m_counter
    i=l
    j=ls
    k=l
    mid=l+size-1# mid is being calculated 
    high=l+2*size-1# high value is being calculated
    if(high > h):
       high=h
    #then same as before the two lists low to mid and mid+1 to high are being merged   
    while( k <= high):
        
        
        m_counter+=1
        if((i<=mid) and (j <= high)):
            if list_[i] <= list_[j]:
                au[k]=list_[i]
                k=k+1
                i=i+1
            else:
                au[k]=list_[j]
                k=k+1
                j=j+1
        elif(j <= high):
            au[k]=list_[j]
            k=k+1
            j=j+1
        elif(i <= mid):
            au[k]=list_[i]
            k=k+1
            i=i+1
        
        
    
    k=low
    while(k <= high):
        list_[k]=au[k]
        k=k+1


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

    size=1
    low=0
    high=len(data)-1
    t0 = time()
    while(size < len(data)):
        
        while(low < (len(data)-size)):
            merge(data,aux_,low,low+size,high,size)
            low=low+size*2
        size=size*2
        low=0
    t1 = time()  
    print("The complexity counter for the top down merge sort for data set of size ",len(data),"is : ",m_counter)
    print("The time taken :",(t1-t0)*1000," ms")
    print("The Sorted Data is as follows :")
    print(data)
