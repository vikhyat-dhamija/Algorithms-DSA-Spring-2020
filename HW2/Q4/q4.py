from time import time
#merge sort
m_counter=0
count=0
#Merge sorting algorithm as in question 3
def merge(l,au,low ,high,mid):
    global m_counter
    
    i=low
    j=mid+1
    k=low

    while( k <= high):
        m_counter+=1
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
        
        
    
    k=low
    while(k <= high):
        l[k]=au[k]
        k=k+1


    return



def merge_sort(l,au, low , high):
        
        if(low < high):
            mid=low + int((high-low)/2)
            merge_sort(l,au,low,mid)
            merge_sort(l,au,mid+1,high)
            merge(l,au,low,high,mid)

        return
#optimised merge sort where the condition commented below is extra
def opt_merge_sort(l,au, low , high):
        global count
        if(low < high):
            mid=low + int((high-low)/2)
            opt_merge_sort(l,au,low,mid)
            opt_merge_sort(l,au,mid+1,high)
            
            if(l[mid+1] < l[mid]):#this condition where the right most element of left array and the first element of right array are compared to check whether two arrays are need to be merged or not
                merge(l,au,low,high,mid)
                count+=1

        return


#quick sort algorithm as in question 5
q_counter=0


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

def partition(arr,low,high):

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
    
    t=arr[low]
    arr[low]=arr[j]
    arr[j]=t
        
    return j



def quicksort_3way(arr,low,high):
     
     if low < high:

        m=median_of_3(arr,low,high)
        
        #swapping of the median value with the lower ones
        t=arr[low]
        arr[low]=arr[m]
        arr[m]=t

        p=partition(arr,low,high)
        
        quicksort_3way(arr,low,p-1)
        quicksort_3way(arr,p+1,high)

     return


#insertion sort as in question 1

i_comparison_counter=0

def insertion_sort(arr):
        global i_comparison_counter

        key_index=1

        if(1 > len(arr)):
            print("size of array is smaller to be sorted")
        else:

            while(key_index < len(arr)):

                ck_ind=key_index
                
                ck_value=arr[ck_ind]
                
                prev_ind=key_index-1
                
                arr[ck_ind]=arr[prev_ind]

                i_comparison_counter+=1
         
                while((prev_ind >= 0 and ck_value < arr[prev_ind]) ):
                    prev_ind-=1
                    ck_ind-=1
                    if(prev_ind < 0):
                        break
                    else:
                        arr[ck_ind]=arr[prev_ind]  
                    i_comparison_counter+=1
                
                arr[prev_ind+1]=ck_value
               
                key_index+=1

        return
#desired array creation
def array_creation():
    data=[]
    i=0

    while(i< 1024):
        data.append(1)
        i+=1
    
    i=0

    while(i < 2048):
        data.append(11)
        i+=1

    i=0

    while(i < 4096):
        data.append(111)
        i+=1
    
    
    i=0

    while(i < 1024):
        data.append(1111)
        i+=1

    return data
#auxiliary array creation is placed in separate function here  
def auxarray_creation(r):

    i=0
    au=[]
    while(i<r):
        au.append(0)
        i+=1
    return au
    
    

if __name__=="__main__":
    
     

     #Insertion sort

     data=array_creation()
     print("The length of the data is : ", len(data))
     print("Insertion Sort------")
     t0=time()
     insertion_sort(data)
     t1=time()
     print("The time taken by insertion sort :",(t1-t0)*1000," ms")
     print("The complexity counter for the insertion sort is : ",i_comparison_counter)
     print("The Data is:")
     #print(data)

     #Merge sort

     data=array_creation()
     au=auxarray_creation(len(data))
     print("Merge Sort------")
     t0=time()
     merge_sort(data,au,0,len(data)-1)
     t1=time()
     
     print("The time taken by normal merge sort :",(t1-t0)*1000," ms")
     print("The complexity counter for the merge sort is : ",m_counter)

     print("The Data is:")
     #print(data)

     #Optimised Merge sort
     m_counter=0
     data=array_creation()
     au=auxarray_creation(len(data))
     print("Optimised Merge Sort------")
     t0=time()
     opt_merge_sort(data,au,0,len(data)-1)
     t1=time()
     print("The time taken by optmised merge sort :",(t1-t0)*1000," ms")
     print("The complexity counter for the optimised merge sort is : ",m_counter)

     print("The Data is:")
    # print(data)

     #3 way quick sort
     #Note that it is commented because for sorted data the maximum recursion depth is reached for it
     '''data=array_creation()
     print("Quick Sort------")
     t0=time()
     quicksort_3way(data,0,len(data)-1)
     t1=time()
     
     print("The time taken by insertion sort :",(t1-t0)*1000," ms")
     print("The complexity counter for the three way quick sort is : ",q_counter)

     print("The Data is:")
     print(data)'''