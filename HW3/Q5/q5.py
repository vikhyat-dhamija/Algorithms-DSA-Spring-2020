#Binary Search Tree Key Value Index representation
#Node Class
class Node: 
    def __init__(self,key,value): 
        self.left = None
        self.right = None
        self.value = value
        self.key=key
        self.size=1
#Root of the tree
root=None
#Insert Function for inserting in the binary serach tree
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

#for putting the key value in the tree
def put(key,value):
    global root
    root=insert_(root,key,value)
#for getting the size of the node ie. the number of nodes including itself
def size(roots):
    if(roots != None):
        return roots.size
    else:
        return 0

#rank function that gives the number of key values smaller tahn the given key
def rank(nod,key):
    if nod != None :
        if nod.key==key:
            return size(nod.left)
        elif nod.key > key:
            return rank(nod.left,key)
        elif nod.key < key:
            return 1+rank(nod.right,key)+size(nod.left)
    else:
        return 0

#select function that gives the key which has given number ( as given by the passed argument) of keys smaller 
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
#finding height
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
#finding the value of a key
def find_key_value(roots,key):
    
    while(roots != None):

        if(roots.key==key):
            return roots.value
        elif(roots.key > key):
            roots=roots.left           
        else:
            roots=roots.right
            
    return -1

#main function
if __name__=="__main__":
    #Note please give the path of the input text file here
    filename="select-data.txt"
    file_=open(filename,"r")
    lines=file_.readlines()
        
    for line in lines:
        line=line.strip()
        put(int(line),int(line))
    
    #rank and select function as desired
    #-----------part a
    print("Part a - Rank Operation")
    print("The result of the operation rank is : ",rank(root,7))
    #-----------part b
    print("Part b - Select Operation")
    print("The result of the operation select is : ",select(root,7))

    




