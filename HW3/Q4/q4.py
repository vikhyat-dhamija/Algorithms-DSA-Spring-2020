#Red-Black BST Implementation
import random
import math
#Class Node of the tree with required elements
class Node: 
    def __init__(self,key,value,color): 
        self.left = None
        self.right = None
        self.value = value
        self.key=key
        self.color=color # 1 means red else black
#Global variables
root=None
first=0
int_path_length=0
level=-1

#to check the color of the node with the color element value
def isred(roots):
    if(roots != None):
        if (roots.color==1):
            return 1
        else:
            return 0
    else:
        return 0
#Left rotation in ordre to make the required conditions of the red black tree to be true
def l_rotate(h):

    x=h.right
    h.right=x.left
    x.left=h
    x.color=h.color
    h.color=1

    return x

#Right rotation in ordre to make the required conditions of the red black tree to be true
def r_rotate(h):
    x=h.left
    h.left=x.right
    x.right=h
    x.color=h.color
    h.color=1

    return x

#Changing of the color when two red nodes are attached to the left and right of a node
def change_colors(h):
    h.color=1
    h.left.color=0
    h.right.color=0

#insert function
def insert_(nod,key,value,color):
    
    if(nod == None):
        if first==1:
            return Node(key,value,0)
        else:
            return Node(key,value,1)
    elif nod.key > key:
        nod.left=insert_(nod.left,key,value,1)
    elif nod.key < key:
        nod.right=insert_(nod.right,key,value,1)
    elif nod.key == key:
         nod.value=value
    
    #Three cases that can appear after addition of the new red colored node in the already balanced red black BST
    #one when this node has red node on the left and we are putting right node on the right
    
    if(isred(nod.left)==0 and isred(nod.right)==1):
        nod=l_rotate(nod)
    if(isred(nod.left)==1 and isred(nod.left.left)==1):
        nod=r_rotate(nod)
    if(isred(nod.left)==1 and isred(nod.right)==1 ):
        change_colors(nod)    
    
    return nod     
#putting the key value
def put(key,value):
    global root
    global first
    first+=1
    root=insert_(root,key,value,1)
#finding the height
def find_key_height(roots,key):
    
    i=1
    while(roots != None):

        if(roots.key==key):
            return i
        elif(roots.key > key):
            roots=roots.left
            i+=1
        else:
            roots=roots.right
            i+=1

    return -1
#finding the key value
def find_key_value(roots,key):
    
    while(roots != None):

        if(roots.key==key):
            return roots.value
        elif(roots.key > key):
            roots=roots.left           
        else:
            roots=roots.right
            
    return -1
#function was made to check the color trail to the particular branch to the key
def color_trail(roots,key):
    
    while(roots != None):
        if(roots.key==key):
            print(roots.color)
            break
        elif(roots.key > key):
            print(roots.color)
            roots=roots.left           
        else:
            print(roots.color)
            roots=roots.right
#function to calculate the path length of the tree
def path_length2(roots):
    global int_path_length
    global level
    if(roots == None):
        level+=1
    else:
        level+=1
        int_path_length+=level       
        path_length2(roots.left)
        level-=1
        path_length2(roots.right)
        level-=1  
     
#main function
if __name__=="__main__":
    #t_list is the sampled list to check the overall results of the experiment
    t_list=[1,10,40,70,100,400,700,1000,2000,3000,5000,6000,7000,8000,10000]    
    for m in range(10000):
        n=m+1
    #for n in t_list:   
        lists=[]
        sums=0
        for i in range(1000):
            l=list(range(n))
            root=None
            random.shuffle(l)
            for j in l:
                put(j,j)
            path_length2(root)
            lists.append(int_path_length/(n))
            sums+=(int_path_length/(n))
            int_path_length=0
            level=-1
        avg=sums/1000                         
        a = [(x - avg)*(x - avg) for x in lists]
        std_dev=math.sqrt(sum(a)/1000)

        print("The average of the average path length of the tree of size : ",n," is : ",avg)            
        print("The std deviation of the average path length of the tree of size : ",n," is : ",std_dev)
    
        
       #need to uncomment the t_list for loop 
       # need to comment the two statements    
    