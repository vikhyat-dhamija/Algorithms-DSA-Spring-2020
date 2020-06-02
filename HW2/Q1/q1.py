comparison_counter=0
i_comparison_counter=0
#global variables for counting the comparisons
from time import time

#Shell Sort
def shell_sort(arr,h):
        global comparison_counter
        #algorithm is self explanatory that we take take one key at h and then move forward with increments to compare it with -h steps elements
        #and this goes on for the whole h to N
        if(h > len(arr)):
            print("h sorting with this value can not be performed")
        else:
            
                key_index=h
                while(key_index < len(arr)):

                    ck_ind=key_index
                    
                    ck_value=arr[ck_ind]
                    
                    prev_ind=key_index-h
                    
                    arr[ck_ind]=arr[prev_ind]
                    
                    comparison_counter+=1                

                    while((prev_ind >= 0 and ck_value < arr[prev_ind]) ):
                        prev_ind-=h
                        ck_ind-=h
                        if(prev_ind < 0):
                            break
                        else:
                            arr[ck_ind]=arr[prev_ind]  
                        comparison_counter+=1
                    arr[prev_ind+h]=ck_value
                     
                    key_index+=1
                
        return
        
def insertion_sort(arr):
        global i_comparison_counter
        # same concept of algorithm as explained above key compared with all previous and then properly inserted
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
        
if __name__=="__main__":
        
    #Reading of data from the file     
    filename="data1.1024"
    file_=open(filename,"r")
    lines=file_.readlines()
    data=[]
    
    for line in lines:
        line=line.strip()
        data.append(int(line))

    
    # Shell sort which reverts to insertion sort
    shell_sort(data,7)
    shell_sort(data,3)
    shell_sort(data,1)

    print(data)
    print(" The number of comparisons done during the shell sort are: ")
    print(comparison_counter)
    
   
    # Shell sort is more effective than Insertion sort
    comparison_counter=0
    i_comparison_counter=0

    #Reading again from the file
    
    file_=open(filename,"r")
    lines=file_.readlines()
    data=[]
    
    for line in lines:
        line=line.strip()
        data.append(int(line))

       
    i_comparison_counter=0
    # Insertion sort
    insertion_sort(data)
    print(" The number of comparisons done during the insertion sort are: ")
    print(i_comparison_counter)

    #Relative (physical wall clock) time taken when using (i) Shell sort that reverts to insertions sort, (ii) Shell sort all the way
    
    #Reading Data from the file
    
    file_=open(filename,"r")
    lines=file_.readlines()
    data=[]
    
    for line in lines:
        line=line.strip()
        data.append(int(line))

    # Shell sort 

    t0 = time() 

    shell_sort(data,7)
    shell_sort(data,3)
    shell_sort(data,1)  

    t1 = time()

    print("The clock time for the execution of shell sort all the way is : ")
    print((t1-t0)*1000)

    #Reading Data from the file
    
    file_=open(filename,"r")
    lines=file_.readlines()
    data=[]

    for line in lines:
        line=line.strip()
        data.append(int(line))

    #Shell sort reverting to Insertion Sort

    t0 = time() 

    
    insertion_sort(data)  

    t1 = time()

    print("The clock time for the execution of  insertion sort is : ")
    print((t1-t0)*1000)
    

    comparison_counter=0
    i_comparison_counter=0

    print("The figures related to Shell sort reverting to insertion after 7-phase")
    #Reading Data from the file
    
    file_=open(filename,"r")
    lines=file_.readlines()
    data=[]

    for line in lines:
        line=line.strip()
        data.append(int(line))

     #Shell sort reverting to Insertion Sort

    t0 = time()
    shell_sort(data,7)
    insertion_sort(data)  
    t1 = time()
    print("The Shell sort phase comparisons : ",comparison_counter)
    print("The Insertion sort phase comparisons : ",i_comparison_counter)
    print("The total comparisons are: ",comparison_counter+i_comparison_counter)
    print("The clock time for the execution of  shell sort ( 7-1) is : ")
    print((t1-t0)*1000)