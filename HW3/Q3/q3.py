#Red-Black BST Implementation
import random
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
red_count=0
black_count=0
first=0

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

#Changing of the color when two red nodes are attached to the left and right
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

#to count the number of red and black nodes
def color_count(roots):
    
    global red_count
    global black_count

    if(roots != None):
        color_count(roots.left)
        if(roots.color==1):
            red_count+=1
        else:
            black_count+=1

        color_count(roots.right)

#Main function
if __name__=="__main__":
    
    n=10000 # u can change the values of n in order to run the experiment
    lists=list(range(0,n))
    
    for j in range (0,100):
        random.shuffle(lists)   
        for i in range(0,n):
            put(lists[i],lists[i])
        color_count(root)
        print("Trial Number : ",j,"  Red nodes : ",red_count," Black nodes : ",black_count , "Per of red : ",(red_count/(red_count+black_count))*100)
        root=None
        red_count=0
        black_count=0


        