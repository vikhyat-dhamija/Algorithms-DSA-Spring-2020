from time import time
#Kruskals Algorithm
first=0

#Edge Class is the data structure which is used to represent the edge which is put into the bags
#Now we have the edge with both points and weight
class edge:
    def __init__(self,x,y,weigh):
        self.x=x
        self.y=y
        self.weigh=weigh

    def one_point(self):
        return self.x

    def other_point(self, v):
        if(v==self.x):
            return self.y
        else:
            return self.x

    def compare_edges(self,edges):
        if(edges.weigh > self.weigh) :
            return 1
        elif edges.weigh < self.weigh :
            return -1
        else:
            return 0

    def display(self):
        print(self.x,"\t",self.y,"\t",self.weigh)

#Union Find to check whether the cycle has been formed or not or to check the connected components so that u do not
#join from the same connected component

def root(p, x): # root finding algorithms same as that of the quick union as the logic is same 
	t = x
	while(t != p[t]):
		t = p[t]
	return t

#Not that the root operation takes the Log N time 
def find( p, x, y): # find function is same as that of the quick union as the logic is same  
    if(root(p, x) == root(p, y)):
        return 1
    else:
        return 0


def quickunion(p,size,x,y): # quick union has a different logic from quick union
        rootx=root(p, x)
        rooty=root(p, y)
        if (size[rootx] <= size[rooty]): #now the sizes are compared and if the destination is smaller then its label is changed else opposite
            p[rootx] = p[rooty]
            size[rooty] += size[rootx] #further the size is also increased
        else:
            p[rooty] = p[rootx]
            size[rootx] += size[rooty]

#NLogN Time algoritm
#Sorting of edges - Merge sort is used here
#merge function
def merge(l,au,low ,high,mid):     
    i=low
    j=mid+1
    k=low
    #k is moving from low to high for merging operation
    while( k <= high):
        
        if((i<=mid) and (j <= high)):
            if l[i].weigh <= l[j].weigh:
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
        
        
    # copying the data from auxiliary array
    k=low
    while(k <= high):
        l[k]=au[k]
        k=k+1


    return

def merge_sort(l,au, low , high):
        #Merge sort recursion based
        if(low < high):
            mid=low + int((high-low)/2)
            merge_sort(l,au,low,mid)
            merge_sort(l,au,mid+1,high)
            merge(l,au,low,high,mid)
        return

#Based on the Union Find it is the Log N algorithm  Here N is the number of vertices
def check_cycle(points,size,edges):

    a=find(points,edges.x,edges.y)
    if a==1:#means that the two end points belong to same connected components which is one of the spanning tree and other of the not in mst
       return 0
    else:
        quickunion(points,size,edges.x,edges.y) 
        #quickunion(points,size,edges.one_point,first)
        return 1

#Now using the sorting and the union find to check whether the new edge to spanning tree form the cycle we now find the MST
#main function
if __name__=="__main__":
    
    #Note please give the path of the input text file here
    filename="dataset1_2.txt"
    #filename="sample.txt"
    file_=open(filename,"r")
    lines=file_.readlines()
    t_verts=int(lines[0].strip())    
    t_edges=int(lines[1].strip())
    
    i=2
    
    #Note that here I have used the list of edges Data structure for the graph as Kruskals is based on sort and check cycle
    #Formation of list of edges
    list_edges=[]
    t_list_edges=[]
    mst_edges=[]

    points=[k for k in range(t_verts)]
    points_size=[1 for k in range(t_verts)]
    
    while i < len(lines):
        line=lines[i].strip()
        edges=line.split()
        list_edges.append(edge(int(edges[0]),int(edges[1]),float(edges[2])))
        t_list_edges.append(edge(int(edges[0]),int(edges[1]),float(edges[2])))
        i+=1
     
    t0=time()
    #ELogE
    #Sorting of the list of edges
    merge_sort(list_edges,t_list_edges,0,len(list_edges)-1)
    
    num=0 

    #Staring kruksal Algorithm for MST
        
    num=0
    x=0
    while x <= len(list_edges)-1 :
        if num >= (t_verts-1):
            break
        else:
            answer=check_cycle(points,points_size,list_edges[x]) #LogV for evry edge so ELog V
            if  answer==1:
                mst_edges.append(list_edges[x])
                num+=1
            
        x+=1
    
    t1=time()
    
    print("--------------Kruksals in action------------------------------")
    print("----------------------This is the result of the Kruskals -------------")
    num=0
    while num < (t_verts-1):
        mst_edges[num].display()
        num+=1
    print("The time taken is : ",t1-t0)
