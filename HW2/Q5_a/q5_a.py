from time import time
#complexity counter
q_counter=0

# function for calculating the median of three that is the middle value in ascending order among the three
def median_of_3(arr,low,high):

    mid=int((low+high)/2)

    if(arr[low] > arr [high]):
        if(arr[high] > arr[mid]):
            return high
        elif(arr[mid]> arr[low] ):
            return low
        else:
            return mid
    else:
        if(arr[low] > arr[mid]):
            return low
        elif(arr[mid] > arr[high] ):
            return high
        else:
            return mid

#partiton function
def partition(arr,low,high):
    # make the lest elemnt as pivot and then scan from left the bigger than pivot and from right side the smaller than pivot
    #and swap them
    global q_counter
    pivot=arr[low]
    i=low+1
    j=high
    while(i <= j):
        while(arr[i] <= pivot ):
            q_counter+=1
            i+=1
            if(i > high):
                break
                          
        while(arr[j] > pivot):    
            q_counter+=1
            j-=1
            if(j < (low+1)):
                break   
        
        if(i < j):
            t=arr[i]
            arr[i]=arr[j]
            arr[j]=t             
        else:
            break        
    #swapping
    t=arr[low]
    arr[low]=arr[j]
    arr[j]=t
        
    return j



def quicksort_3way(arr,low,high):
     
     if low < high:
        #median finding out
        m=median_of_3(arr,low,high)
        
        #swapping of the median value with the lower ones
        t=arr[low]
        arr[low]=arr[m]
        arr[m]=t
        #partition function 
        p=partition(arr,low,high)
        #then quick sort recursively for both left and right side of the pivot
        quicksort_3way(arr,low,p-1)
        quicksort_3way(arr,p+1,high)

     return
           



if __name__=="__main__":
    
    filename="data1.1024"
    file_=open(filename,"r")
    lines=file_.readlines()
    data=[]
    
    for line in lines:
        line=line.strip()
        data.append(int(line))
    
    t0 = time()    
    quicksort_3way(data,0,len(data)-1)
    t1 = time()
    print("The complexity counter for the 3 way quick sort without insertion ",len(data),"is : ",q_counter)
    print("The time taken :",(t1-t0)*1000," ms")
    print(data)

    