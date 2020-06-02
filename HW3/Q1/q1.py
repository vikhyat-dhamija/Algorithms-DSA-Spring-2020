import math
#Node Class with the constructor to initialise the Node
class Node: 
    def __init__(self,key,value): 
        self.left = None
        self.middle=None
        self.right = None
        self.key = [None]*2
        self.value=[None]*2
        self.key[0]=key
        self.value[0]=value
#Global Variables used i.e. root is the root of the tree and flag and m are for internal communication between the insertion 
#and the rearrange module that whether rearrangement has to be done or not
root=None
flag=0
m=0
# sorting has been created as a separate function to order the keys and values in the nodes
def sorting(keys,values,lenn):
    if(keys[1] < keys[0]):
       k=keys[1]
       v=values[1]
       keys[1]=keys[0]
       values[1]=values[0]
       keys[0]=k
       values[0]=v
    if(lenn==3):
        if(keys[2] < keys[1]):
            k=keys[2]
            v=values[2]
            keys[2]=keys[1]
            values[2]=values[1]
            keys[1]=k
            values[1]=v
        if(keys[1] < keys[0]):
            k=keys[1]
            v=values[1]
            keys[1]=keys[0]
            values[1]=values[0]
            keys[0]=k
            values[0]=v
    
#Compare function is to provide the position of the new node to be inserted 1,2,3 ie before left , in the middle and after right
def compare(l,key):
    if l[0]!= None and key < l[0] :
        return 1
    elif l[1]!= None and key > l[0] and key < l[1] :
        return 2
    else:
        return 3
#rearrange function the most complicated and the most important part
#as its functionality leads to balancing
def rearrange(nod ,x):
    global m
    global flag
    #when any of the key of the node is not zero and the key has come from botton for rearrangement
    if (nod.key[0]!=None and nod.key[1]==None) or (nod.key[1]!=None and nod.key[0]==None):
        
        if(nod.key[0] > x.key[0]):
            nod.key[1]=nod.key[0]
            nod.value[1]=nod.value[0]
            nod.key[0]=x.key[0]
            nod.value[0]=x.value[0]          
            nod.middle=x.right
            nod.left=x.left
        else:
            nod.key[1]=x.key[0]
            nod.value[1]=x.value[0]
            nod.middle=x.left
            nod.right=x.right
        flag=0
        return nod
    #when keys of the node are not zero and the key has come from botton for rearrangement
    elif nod.key[0]!=None and nod.key[1]!=None:

        pos=compare(nod.key,x.key[0])

        if pos==1:
            temp_node_h=Node(nod.key[0],nod.value[0])
            temp_node_l=Node(x.key[0],x.value[0])
            temp_node_r=Node(nod.key[1],nod.value[1])
            temp_node_l.left=x.left
            temp_node_l.right=x.right
            temp_node_r.left=nod.middle
            temp_node_r.right=nod.right
        elif pos==2:
            temp_node_h=Node(x.key[0],x.value[0])
            temp_node_l=Node(nod.key[0],nod.value[0])
            temp_node_r=Node(nod.key[1],nod.value[1])
            temp_node_l.left=nod.left
            temp_node_l.right=x.left
            temp_node_r.left=x.right
            temp_node_r.right=nod.right
        else:
            temp_node_h=Node(nod.key[1],nod.value[1])
            temp_node_l=Node(nod.key[0],nod.value[0])
            temp_node_r=Node(x.key[0],x.value[0])
            temp_node_r.left=x.left
            temp_node_r.right=x.right
            temp_node_l.left=nod.left
            temp_node_l.right=nod.middle
        
        temp_node_h.left=temp_node_l
        temp_node_h.right=temp_node_r
        if(nod != root):
            flag=1           
        else:
            flag=0
            
        return temp_node_h
#insert function for the insertion of the key value
def insert_(nod,key,value):
        global flag
        global m
        # first we check that we are at the empty tree
        if(nod == None):
            return Node(key,value)
        #then we check that whether the same key is there or not and hence update its value
        if(nod.key[0]==key or nod.key[1]==key):
            if(nod.key[0]==key):
                nod.value[0]=value 
            else:
                nod.value[1]=value  
            return nod
        # Then we go to the leaf node for puuting the key value
        if nod.left == None and nod.right==None :
            if nod.key[0] == None and nod.key[1]== None :
                nod.key[0]=key
                nod.value[0]=value
            elif nod.key[0] != None and nod.key[1]== None:
                nod.key[1]=key
                nod.value[1]=value
                sorting(nod.key,nod.value,2)    
            elif nod.key[1] != None and nod.key[0]== None:
                nod.key[0]=key
                nod.value[0]=value
                sorting(nod.key,nod.value,2)
            else:
                l=[None]*3
                s=[None]*3
                l[0]=nod.key[0]
                l[1]=nod.key[1]
                l[2]=key
                s[0]=nod.value[0]
                s[1]=nod.value[1]
                s[2]=value
                #l.sort()
                #s.sort()
                sorting(l,s,3)
                roots=Node(l[1],s[1])
                roots.left=Node(l[0],s[0])
                roots.right=Node(l[2],s[2])
                m+=1
                return roots
        #if we are not at the leaf then we traverse the tree to get into the right position where the key-value has to be inserted    
        else:
            pos=compare(nod.key,key)
            if pos==1 :
                x=insert_(nod.left,key,value)
                if((m== 1 and flag==0)) :
                    nod.left=x
                else:
                    nod=rearrange(nod,x)
                    m=1
            elif pos==3:
                x=insert_(nod.right,key,value)
                if((m== 1 and flag==0) ):
                    nod.right=x
                else:
                    nod=rearrange(nod,x)
                    m=1
            elif pos==2:
                x=insert_(nod.middle,key,value)
                if((m== 1 and flag==0)):
                    nod.middle=x
                else:
                    nod=rearrange(nod,x)
                    m=1
        return nod
#put function for putting the key values in the tree
def put(key,value):
    global root
    global flag
    
    root=insert_(root,key,value)
#in order traversal
def inorder_traversal(roots):

    if(roots != None):
        inorder_traversal(roots.left)
        if(roots.key[0] != None):          
            print("The value of the Key : ",roots.key[0])
            print("The value of the Value : ",roots.value[0])
        inorder_traversal(roots.middle)
        if(roots.key[1] != None):           
            print("The value of the Key : ",roots.key[1])
            print("The value of the Value : ",roots.value[1])
        inorder_traversal(roots.right)
#level wise printing of the tree
def level_print(roots,num):
    level=1
    non=1
    l=[]
    m=[]
    m.append(roots)
    while(level <= math.log2(num)):
        #Putting children of the node
        l=[]
        print("The Level ",level,":")
        i=1
        while(i <= non):
            if(m[i-1]!= None):
                
                print("\t",m[i-1].key)         
                l.append(m[i-1].left)
                l.append(m[i-1].middle)
                l.append(m[i-1].right)
            else:
                l.append(None)
                l.append(None)
                l.append(None)
            i+=1
        non*=3
        level+=1
        m=l
#for getting the value of the key
def get(nod,key):

    if(nod != None):
        if(nod.key[0]==key or nod.key[1]==key):
            if(nod.key[0]==key):
                return nod.value[0]
            else:
                return nod.value[1]
        else:
            pos=compare(nod.key,key) 
            if( pos==1):
               m=get(nod.left,key) 
            elif(pos==2):
               m=get(nod.middle,key)
            else:
               m=get(nod.right,key)
            return m

if __name__=="__main__":
    #note that any of the input mst can be chosen for the input to the program one is random and one is the sorted
    #mst = [13,7,13,24,15,4,29,4,20,16,19,1,5,22,5,31,32,2,3,25,27]
    mst=[1,2,3,4,5,6,7,8,9,9,9,10,11,12,13,14,15,16,17]
    for item in mst:
	    put(item,item)
    print("----------Inorder Traversal----------")
    inorder_traversal(root)
    print("-----------------The Level wise Tree-----------")
    level_print(root,len(mst))

    #Getting the Value of Key in order to check the get function
    print("-------To check the Get value Function-----------")
    k=input("Please input the key to get the value")
    v=get(root,int(k))
    if(v != None):
       print("The value of the Key : ",k," is : ",v)
    else:
       print("The key is not present in the tree")