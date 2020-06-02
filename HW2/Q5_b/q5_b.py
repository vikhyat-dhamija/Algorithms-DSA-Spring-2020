from time import time
cut_off=7#cut off made the global variable
qi_counter=0
#complexity counter
#same median function as in previous quick sort question 5 a
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


#Partition Function
def partition_i(arr,low,high):
    global qi_counter
    pivot=arr[low]
    i=low+1
    j=high
    while(i <= j):
        while(arr[i] <= pivot ):
            qi_counter+=1
            i+=1
            if(i > high):
                break
                          
        while(arr[j] > pivot):    
            qi_counter+=1
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


#Insertion sort as in question 1
def insertion_sort(arr,low,high):

    global qi_counter
             
    key_index=low+1

    while(key_index < (high+1)):

        ck_ind=key_index
                    
        ck_value=arr[ck_ind]
                    
        prev_ind=key_index-1
                    
        arr[ck_ind]=arr[prev_ind]

                    
        qi_counter+=1
        while((prev_ind >= low and ck_value < arr[prev_ind]) ):
            qi_counter+=1
            prev_ind-=1
            ck_ind-=1
            if(prev_ind < low):
                break
            else:
                arr[ck_ind]=arr[prev_ind]  
            
        arr[prev_ind+1]=ck_value
                
        key_index+=1

    return        

             
#quick sort main function with slight differnce for applying the insertion sort cut off
def quicksort_3way_insertion(arr,low,high):
     
     global cut_off
     
     if low < high:
        #here when the size of array on which sort has to be done is the size of the cut off then that array is sorted from the insertion sort method
        if((high-low+1) <= cut_off):
            insertion_sort(arr,low,high)
        else:

            m=median_of_3(arr,low,high)
            
            #swapping of the median value with the lower ones
            t=arr[low]
            arr[low]=arr[m]
            arr[m]=t

            p=partition_i(arr,low,high)
            quicksort_3way_insertion(arr,low,p-1)
            quicksort_3way_insertion(arr,p+1,high)

     return

if __name__=="__main__":
    
    filename="data0.16384"
    file_=open(filename,"r")
    lines=file_.readlines()
    data=[]
   
    for line in lines:
        line=line.strip()
        data.append(int(line))

    t0 = time()    
    quicksort_3way_insertion(data,0,len(data)-1)
    t1 = time()
    
    print("The complexity counter for the 3 way quick sort with insertion cut off  with data size of ",len(data),"is : ",qi_counter)
    print("The time taken :",(t1-t0)*1000," ms")
    print("The Sorted Data is as follows :")
    print(data)
    

