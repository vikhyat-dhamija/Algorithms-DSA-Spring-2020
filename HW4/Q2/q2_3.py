from time import time
#Edge Class 
#Now we have the edge with both points of edge and the weights 
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

#Binary Heap Data Structure used in the implementation of the algorithm
class bin_heap_pq:

    def __init__(self,v): 
        self.list_=[edge(1000,1000,1000) for k in range(1500)]
        self.n=0

    def insert_key(self,key):
        self.n+=1
        self.list_[self.n]=key
        self.swim_up(self.n)

        
    def sink_down(self):
        if(self.n >= 1):
            i=1
            while(i <= int(self.n/2)):
                if((2*i+1)<= self.n):
                    pos=self.less(2*i,2*i+1)
                else:
                    pos=2*i                    
                if(self.list_[i].weigh > self.list_[pos].weigh):
                    self.swap(i,pos)
                i=pos
                
    def delete_min(self):
        
        if self.n==1:
            min=self.list_[1]
            self.list_[1]=edge(1000,1000,1000)
            self.n-=1
            return min
        elif(self.n > 1):
            min=self.list_[1]
            self.list_[1]=self.list_[self.n]
            self.list_[self.n]=edge(1000,1000,1000)
            self.n=self.n-1
            self.sink_down()
            
            return min


    def swim_up(self,num): # that is while insertion
        parent=int(num/2)
        while(parent >= 1):
            if self.list_[parent].weigh > self.list_[num].weigh:
               self.swap(parent,num)
            parent=int(parent/2)
            num=int(num/2)

    def less(self,x,y):
        if self.list_[x].weigh < self.list_[y].weigh:
            return x
        else:
            return y

    def swap(self,x,y):
        t=self.list_[x]
        self.list_[x]=self.list_[y]
        self.list_[y]=t

    def display(self):
        for i in range(self.n):
            print(i+1)
            self.list_[i+1].display()

#Same the list of adjacent edges
class bag:
    
    def __init__(self):
        self.list_v=[]
        

    def appends(self,x,y,w):
        e=edge(x,y,w)
        self.list_v.append(e)
        
    def length(self):
        return len(self.list_v)
    
    def display_bag(self):
        for i in range(len(self.list_v)):
            self.list_v[i].display()

#Graph Data Structure - based on the first question program
class Graph: 

    marked=[]
    parent=[]
    c_marked=[]
    c_parent=[]
    is_cyclic=0
   
    def __init__(self,vert):
        self.vertices= [bag() for i in range(vert)]
        self.marked=[0 for i in range(vert)]
        self.parent=[-1 for i in range(vert)]
        self.c_marked=[0 for i in range(vert)]
        self.c_parent=[-1 for i in range(vert)]
        self.nov=vert
        self.is_cyclic=0
        
    
    def edge_formation(self,x,y,w):
        self.vertices[x].appends(x,y,w)
        self.vertices[y].appends(x,y,w)


    def adjacent_vertices(self,x):
        return self.vertices[x]


    # Depth first serach algorithm
    def dfs(self,m):                  
        adj=self.adjacent_vertices(m).list_bag()
        self.marked[m]=1
        #print(m)
        j=0
        while j < len(adj):
            if self.marked[adj[j]] != 1 :                
                self.dfs(adj[j])
                self.parent[adj[j]]=m
            j+=1
             
   
    def display(self):
        for k in range(self.nov):
            i=0
            adj_list=self.adjacent_vertices(k).list_bag()
            while i < len(adj_list):
                print("Edge: ",k,"---->",adj_list[i])
                i+=1 




if __name__=="__main__":
        
        #Please put the path name in case the path name is different
        filename="dataset1_2.txt"
        file_=open(filename,"r")
        lines=file_.readlines()
        t_verts=int(lines[0].strip())    
        t_edges=int(lines[1].strip())
        
        #Graph Formation
        i=2
        gr=Graph(t_verts)
        
        while i < len(lines):
            line=lines[i].strip()
            edges=line.split()
            gr.edge_formation(int(edges[0]),int(edges[1]),float(edges[2]))
            i+=1
        
        #Data Structure of Binary Heap
        pq=bin_heap_pq(t_edges+1)
        
        marked=[0 for k in range(t_verts)]
        mst_=[]
        #list of edges that need to be put up in the MST
        
        t0=time()
        #Starting from the first node
        marked[0]=1
        b_edges=gr.adjacent_vertices(0)

        for i in range(len(b_edges.list_v)):
            if(marked[b_edges.list_v[i].other_point(0)]!=1):
                 pq.insert_key(b_edges.list_v[i])

        # here first we insert the adjacent edges in the priority queue of the one emanating from 0
              
    # Running the loop till we scan through all edges
        while(pq.n > 0):
            
            first_e=pq.delete_min() # here we delete the minimum edge so it is a Log N operation for the first case it will the one starting from 0
            
            x=first_e.one_point()
            y=first_e.other_point(x)
            
            if(marked[x]==0 or marked[y]==0): # here after pulling out we check whether any of the vertices are unmarked
                # Append the min edge in the MST
                mst_.append(first_e)
                #If one that is unmarked is x then 
                if(marked[x]==0):
                    marked[x]=1 # we mark that vertex as it is a part of Mst now  
                    b_edges=gr.adjacent_vertices(x) # Bring out the adjacent edges of that vertex put them in the priority queue when the 
                    #other points of the edges apart from x are not marked i.e. are not visited
                    for i in range(len(b_edges.list_v)):
                        if(marked[b_edges.list_v[i].other_point(x)]!=1):
                            pq.insert_key(b_edges.list_v[i])
                
                #the same logic is here for this part when y is not marked
                if(marked[y]==0):
                    marked[y]=1
                    b_edges=gr.adjacent_vertices(y)
                    for i in range(len(b_edges.list_v)):
                        if(marked[b_edges.list_v[i].other_point(y)]!=1):
                            pq.insert_key(b_edges.list_v[i])
            
        t1=time()

        #Printing of the result    
        print("--------------Prims Lazy approach in action ------------------------------")
        print("----------------------This is the result of the Prims Lazy approach -------------")
        for i in range(len(mst_)):
            mst_[i].display()
        
        print("The time taken is : ",t1-t0)