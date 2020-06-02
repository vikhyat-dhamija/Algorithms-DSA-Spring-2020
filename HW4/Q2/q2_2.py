from time import time
#This is the edges and the point being returned so data structure for that
class returns:
    def __init__(self,e,p):
        self.e=e
        self.p=p

#Indexed Binary Heap Data Structure- here the key is the edge and the index is the vertex for which respect it has been inserted
class ipq:

    def __init__(self,v):
        self.verts=[-1 for k in range(v)]
        self.list_=[edge(-1,-1,1000) for k in range(v)]
        self.index_=[-1 for k in range(v)]
        self.n=-1
    
    # here we insert the edge in the particular index
    def insert_key(self,key,index):
        
        self.n+=1
        self.list_[self.n]=key
        self.verts[self.n]=index
        self.index_[index]=self.n     
        self.swim_up(self.n)
        
    # here we decrease the value of the edge in case of already existing edge for a givn vertex which is the index 
    def decrease_key(self,key,index):
        if self.n >= self.index_[index] :
            self.list_[self.index_[index]]=key
            self.swim_up(self.index_[index])

    # sink down when we delete we puul out the last from the heap to first and then sink down            
    def sink_down(self):
        if(self.n >= 0):
            i=0
            while(i <= int((self.n-1)/2)):               
                if((2*i+2)<= self.n):
                    pos=self.less(2*i+1,2*i+2)
                else:
                    pos=2*i+1                  
                if(self.list_[i].weigh > self.list_[pos].weigh):
                    self.swap(i,pos)
                i=pos
    
    #delete Minimum i.e the first one of the Minimum Heap
    def delete_min(self):       
        
        if self.n==0:
            min_e=self.list_[0]
            min_v=self.verts[0]
            self.list_[0]=edge(-1,-1,1000)
            self.index_[self.verts[0]]=-1
            self.verts[0]=-1
            self.n-=1
            return returns( min_e,min_v)

        elif(self.n > 0):
            min_e=self.list_[0]
            min_v=self.verts[0]
            #Here first vertex is deleted so
            self.index_[self.verts[0]]=-1
            self.verts[0]=-1            
            self.list_[0]=self.list_[self.n]
            self.verts[0]=self.verts[self.n]
            self.index_[self.verts[0]]=0
            self.list_[self.n]=edge(-1,-1,1000)
            self.n=self.n-1
            self.sink_down()
            self.verts[self.n+1]=-1
            return returns( min_e,min_v)

    #Swim Up as we insert at the bottom and then swim up
    def swim_up(self,num): # that is while insertion       
        parent= -1 if (num-1) < 0 else int((num-1)/2)
        while(parent >= 0):
            if self.list_[parent].weigh > self.list_[num].weigh:
                self.swap(parent,num)
            parent= -1 if (parent-1) < 0 else int((parent-1)/2)
            num=-1 if (num-1) < 0 else int((num-1)/2)

    # comparison of edges
    def less(self,x,y):
        if self.list_[x].weigh < self.list_[y].weigh:
            return x
        else:
            return y
    
    # swapping of edges
    def swap(self,x,y):
        t=self.list_[x]
        self.list_[x]=self.list_[y]
        self.list_[y]=t

        t=self.verts[x]
        self.verts[x]=self.verts[y]
        self.verts[y]=t

        self.index_[self.verts[x]]=x
        self.index_[self.verts[y]]=y
    

    # display
    def display(self):
        for i in range(self.n+1):
            self.list_[i].display()
        
        for i in range(8):    
            print(self.index_[i])
    
    #size of the prioirity queue
    def size(self):
        return (self.n+1)
    
    # check whether the vertex is empty or not
    def check_v_empty(self,v):
        if self.index_[v]==-1:
            return 1
        else:
            return 0
    # Get the weight of the particular index vertex edge
    def get_index_key(self,v):
        return self.list_[self.index_[v]].weigh


#Edge Class as was the only one point in the bag in the previous simple undirected graph
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

# Bag of edges as usual in our graph structure
class bag:
    def __init__(self):
        self.list_v=[]
        self.weight_=[]
    #Append
    def appends(self,x,y,w):
        e=edge(x,y,w)
        self.list_v.append(e)
        self.weight_.append(w)
    # length of the bag
    def length(self):
        return len(self.list_v)
    # display the bag
    def display_bag(self):
        for i in range(len(self.list_v)):
            self.list_v[i].display()

#Graph Data Structure as used in other questions
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
        
    #edge formation
    def edge_formation(self,x,y,w):
        self.vertices[x].appends(x,y,w)
        self.vertices[y].appends(x,y,w)

    #Adjacent vertices
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
             
    # Dispaly
    def display(self):
        for k in range(self.nov):
            i=0
            adj_list=self.adjacent_vertices(k).list_bag()
            while i < len(adj_list):
                print("Edge: ",k,"---->",adj_list[i])
                i+=1 

# main starts
if __name__=="__main__":
    
        #Note please give the path of the input text file here
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
        
        #Start of the Prims algorithm with the eager approach
        
        #Variables for initiation
        bags=0
        ipq_=ipq(t_verts)#Indexed Priority queue with length of vertices
        visited=[0 for k in range(t_verts)]
        mst_=[]
        count=0
        # MST is the list of edges in the MST
        
        t0=time()

        #for k in range(t_verts):
        while(count < (t_verts)): # here checking the count whether it has become equal to (V) as 0 is also counted otherwise number of edges(V-1) in MST
        #if 1:
            if count==0:
                k1=0  # first case the vertex is 0
                count+=1 
            else:
                r=ipq_.delete_min() # else we are extracting the minimum out of heap
                k1=r.p # getting the point from the return dat structure
                mst_.append(r.e) # append that edge 
                count+=1 # incrementing the count as the edge has been added 
            
            if count < (t_verts-1):
                # now when we do not have all the edges for the MST 
                visited[k1]=1   #Here we mark the point we got from return as visited
                bags=gr.adjacent_vertices(k1) # extracting the adjacent edges out in the bag
                

                # then we open the bag of edges for that point 
                for m in range(bags.length()):#Open each bag for each vertices
                    
                    v1=bags.list_v[m].one_point()
                    v2=bags.list_v[m].other_point(v1)
                    
                    if v1==k1:
                        x=v2
                    else:
                        x=v1
                    #get the other points

                    # Check whether the vertex is alreday visited if not check 
                    if visited[x]!=1:
                        # if the index that is the edge corresponding to that vertex is alreday there then insert 
                        if ipq_.check_v_empty(x)==1:    
                            ipq_.insert_key(bags.list_v[m],x)#insert the adjacent points to one vertex in the priority key
                        else:
                            #other wise decrease based on weights comparison
                            if (ipq_.get_index_key(x) > bags.weight_[m]):
                                ipq_.decrease_key(bags.list_v[m],x)
                                
        t1=time()

        print("--------------Prims Eager approach in action------------------------------")
        print("----------------------This is the result of the Prims Eager approach -------------")            
        
        for i in range(len(mst_)):
            mst_[i].display()
        
        print("The time taken is : ",t1-t0)



