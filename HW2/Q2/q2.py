b_counter=0
m_counter=0
#Complexity Counters

#Two loops for creating pairs and then finding whether they are in reverse order or not
def ktd_q(arr1,arr2):
    global b_counter
    i=0
    j=0
    kt_dis=0
    
    while(i < len(arr1)):
        j=i+1
        while(j < len(arr2)):
            b_counter+=1#complexity Counter
            if(((arr1[j]-arr1[i]) * (arr2[j]-arr2[i])) < 0):
                kt_dis+=1
            j+=1
        i+=1

    return kt_dis

#merge function
def i_merge(l,au,low ,high,mid,count):
    global m_counter
    i=low
    j=mid+1
    k=low

    while( k <= high):
        
        m_counter+=1# complexity counter

        if((i<=mid) and (j <= high)):
            if l[i] <= l[j]:
                au[k]=l[i]
                k=k+1
                i=i+1
            else:
                au[k]=l[j]
                k=k+1
                j=j+1
                count[0]+=(mid-i+1)
        elif(j <= high):
            au[k]=l[j]
            k=k+1
            j=j+1
        elif(i <= mid):
            au[k]=l[i]
            k=k+1
            i=i+1
            
        
    
    k=low
    while(k <= high):
        l[k]=au[k]
        k=k+1


    return


#merge sorting 
def i_merge_sort(l,au, low , high,c):
        
        if(low < high):

            mid=low + int((high-low)/2)
            i_merge_sort(l,au,low,mid,c)
            i_merge_sort(l,au,mid+1,high,c)
            i_merge(l,au,low,high,mid,c)

        return


if __name__=="__main__":
    
    m_dis=[0]
    filename="data0.1024"
    file_=open(filename,"r")
    lines=file_.readlines()
    data_=[]
    
    for line in lines:
        line=line.strip()
        data_.append(int(line))
        
    
    filename="data1.1024"
    file_=open(filename,"r")
    lines=file_.readlines()
    data=[]
    aux_=[]
    
    for line in lines:
        line=line.strip()
        data.append(int(line))
        aux_.append(0)
    
    d=ktd_q(data,data_)

    i_merge_sort(data,aux_,0,len(data)-1,m_dis)

    

    print("Kendal Tau Distance between data0 and data1 datasets of size ",len(data)," is:")
    
    print("Using the Brute force quadratic algorithm :", d)
    
    print("Using the merge sort based counting inversions method :",m_dis[0])
    
    print("The complexity counter of brute force is :",b_counter)
    
    print("The complexity counter of merge based method is :",m_counter)