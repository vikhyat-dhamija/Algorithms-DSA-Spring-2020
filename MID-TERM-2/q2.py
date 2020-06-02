#Method 2------ Sort and Scan------------------------the below is O(N^2) like regular scanning like selection sort
#But this method can be improved if we use Merge Sort then N Log N for sorting plus N for scanning of uniqueness then whole algorithm will be
#--- N Log N--------here bubble sort is used
def sort_(temp):
    i=0
    f=len(temp)-1

    while (f-i)>0:
        k=0    
        while k < (f-i):
            if temp[k] > temp[k+1]:
                t=temp[k]
                temp[k]=temp[k+1]
                temp[k+1]=t
            k=k+1
        i=i+1

    return temp    

#Sort and Scan comparing 1 value with previous value
def check_unique(temp):
    temp=sort_(temp)
    i=1
    flag=1
    while i < len(temp) :
        if temp[i]==temp[i-1]:
            flag=0
            break
        else:
            pass
        i+=1
    return flag

# Main function starting
if __name__=="__main__":

    # Code Regarding the Hashing Function
    input_list=['S','E','A','R','C','H','X','M','P','L']
    pos_list=[]

    # Finding the positions of the characters in the alphabat list
    for i in range(len(input_list)):
        pos_list.append((ord(input_list[i])-ord('A')+1))
    
    # Two analytical aspects were -----

    #-----------One----------------
    # value in modulus operator with can result in value 0 to M-1 
    # A can take value nM+(0 to M-1) because for values of n=(0,1,2.....)
    # we have taken the value of n=0 as others are just same as other n as both lead to same resulting value of the hash function
    
    #-------------Two-----------------
    # Minimum 10 values are needed in the Table for getting the 10 index in the table so minimum value of M can be 10
    # As we need M bins we need to have at least value of m as 10 so strating with value of m =10
    m_=10
    a_list=[]
    flag=0

    # Loop for checking all values of M which will stop for smallest value of M for which we find certain values of A so as all the hashed index values are unique
    while(1):  
        #Iteration for the values of A which can range    
        for j in range(m_):
            # Now we need to check that for partcular value of M and A we have unique values of hashed values for 10 input characters
            temp=[((j*x) % m_) for x in pos_list]
            
            
            #Method 1------using in buit function ---- we do not know the complexity so i used the method 2
            #To check whether all the values are unique i.e the set the unique values in the list have length as the initial list
            '''if(len(set(temp))==len(input_list)):
                a_list.append(j)
                flag=1'''

            if(check_unique(temp)==1):
                a_list.append(j)
                flag=1
        
        if(flag==0):
            m_=m_+1
        else:
            break  

    #Print the Results
    print("The results are :")
    print("For the smallest value of M which is : ",m_)
    print("The  values of A are : ",a_list)






     



