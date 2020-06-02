
import random
import sys

#Node Class with the constructor to initialise the Node
class Node: 
    def __init__(self,key,value): 
        self.left = None
        self.right = None
        self.value = value
        self.key=key
        self.size=1
#Global Variables used i.e. root is the root of the tree , int_path_length denotes the internal path length and level as the level of the tree
root=None
int_path_length=0
level=-1
#insert with the size updation
def insert_(nod,key,value):
    
    if(nod == None):
        return Node(key,value)
    elif nod.key > key:
        nod.left=insert_(nod.left,key,value)
    elif nod.key < key:
        nod.right=insert_(nod.right,key,value)
    elif nod.key == key:
         nod.value=value
    
    nod.size=1
    if(nod.left != None):
        nod.size+=nod.left.size
    if(nod.right != None):
        nod.size+=nod.right.size

    return nod     
#in order traversal
def inorder_traversal(roots):

    if(roots != None):
        inorder_traversal(roots.left)
        print("The value of the Key : ",roots.key," Value : ",roots.value," and size is : ", roots.size)
        inorder_traversal(roots.right)
#put function for putting the key value
def put(key,value):
    global root
    root=insert_(root,key,value)
#size function to return the size of the node
def size(roots):
    if(roots != None):
        return roots.size
    else:
        return 0

#select function for finding the key gretaer than the given number of keys passed as the parameter   
def select(nod,k):

    if nod != None :
        if k == (size(nod.left)):
            return nod.key
        elif k < (size(nod.left)):
            return select(nod.left,k)
        elif k > (size(nod.left)):
            return select(nod.right,k-size(nod.left)-1)
    else:
        return -1

#to find the height of the key in atree
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

# kind of get function to find the value of the key
def find_key_value(roots,key):
    
    while(roots != None):

        if(roots.key==key):
            return roots.value
        elif(roots.key > key):
            roots=roots.left           
        else:
            roots=roots.right
            
    return -1

#internal path length using recursion
def path_length(roots):

     if(roots != None):
        x=path_length(roots.left)+path_length(roots.right)+roots.size-1
        return x
     else:
        return 0
#internal path length using node by node traversal without recursion
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
    

if __name__=="__main__":
    # for changing the recursion limit
    sys.setrecursionlimit(100000000)
    #Note Please uncomment the prints below to see the recursion based path length also 
    root=None
    #for random elements
    print("----------------------For the random elements-------------------")
    m=2
    while(m<=8192):
        
        l=list(range(m))
        random.shuffle(l)
        for i in l:
             put(i,i)
        #print("The tree with size : ", m ," the average path lenth is : ",path_length(root)/root.size)
        path_length2(root)
        print("The tree with size : ", m ," the average path lenth is : ",int_path_length/root.size)
        int_path_length=0
        level=-1
        root=None
        m*=2
    
    
    #for sorted elements
    print("----------------------For the sorted elements-------------------")
    m=2
    while(m<=8192):
        x=0
        while(x<m):
            put(x,x)
            x+=1
        #print("The tree with size : ",m," the average path lenth is : ",path_length(root)/root.size)
        path_length2(root)
        print("The tree with size : ", m ," the average path lenth is : ",int_path_length/root.size)
        root=None
        int_path_length=0
        level=-1
        m*=2
    