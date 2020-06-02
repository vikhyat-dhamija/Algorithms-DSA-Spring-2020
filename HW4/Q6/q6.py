# Return is the structure used for returning the point and the edge
class returns:
    def __init__(self,e,p):
        self.e=e
        self.p=p


#Indexed Binary Heap Data Structure same as used in the Prims Eager Approach
class ipq:
    # Initialisation of lists used 
    def __init__(self,v):
        self.verts=[-1 for k in range(v)] # Vertices 
        self.list_=[edge(-1,-1,1000) for k in range(v)]#keys i.e the edges
        self.index_=[-1 for k in range(v)] # index 
        self.n=-1#Initial counter for insertion
    
    #Insertion just insert at the last and then swim up
    def insert_key(self,key,index):
        
        self.n+=1
        self.list_[self.n]=key
        self.verts[self.n]=index
        self.index_[index]=self.n     
        self.swim_up(self.n)
        
    #Decrease key just replace the key at particular index and then swim up to maintain heap
    def decrease_key(self,key,index):
        if self.n >= self.index_[index] :
            self.list_[self.index_[index]]=key
            self.swim_up(self.index_[index])

    # Swim down is being performed when after deletion the last member of the heap become first then we have to do the sink down operation            
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
    
    # Delete minimum delete the first that is the minimum and then insert the last one as the first one and then sink down
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

    # swim up in case of decrease key and the insert key
    def swim_up(self,num): # that is while insertion       
        parent= -1 if (num-1) < 0 else int((num-1)/2)
        while(parent >= 0):
            if self.list_[parent].weigh > self.list_[num].weigh:
                self.swap(parent,num)
            parent= -1 if (parent-1) < 0 else int((parent-1)/2)
            num=-1 if (num-1) < 0 else int((num-1)/2)

    # Less comparison has to be performed
    def less(self,x,y):
        if self.list_[x].weigh < self.list_[y].weigh:
            return x
        else:
            return y

    # swapping has to be performed 
    def swap(self,x,y):
        t=self.list_[x]
        self.list_[x]=self.list_[y]
        self.list_[y]=t

        t=self.verts[x]
        self.verts[x]=self.verts[y]
        self.verts[y]=t

        self.index_[self.verts[x]]=x
        self.index_[self.verts[y]]=y
    
    #Display of the edges in the indexed priority queue
    def display(self):
        for i in range(self.n+1):
            self.list_[i].display()
        
        for i in range(8):    
            print(self.index_[i])
    
    # Size of the priority queue
    def size(self):
        return (self.n+1)
    
    # Check whether any particular index is empty or not 
    def check_v_empty(self,v):
        if self.index_[v]==-1:
            return 1
        else:
            return 0
   
    # Get the weight of the index or the vertex in our algorithm 
    def get_index_key(self,v):
        return self.list_[self.index_[v]].weigh


#Edge Class Data Structure for holding the vertex and the weight
class edge:
    
    def __init__(self,x,y,weigh):
        self.x=x
        self.y=y
        self.weigh=weigh

    def from_point(self):
        return self.x

    def other_point(self):
        return self.y

    def compare_edges(self,edges):
        if(edges.weigh > self.weigh) :
            return 1
        elif edges.weigh < self.weigh :
            return -1
        else:
            return 0

    def display(self):
        print(self.x,"\t",self.y,"\t",self.weigh)

#Bag Class Data Structure for holding the edges for each vertex it is the adjacency List holding the edges
class bag:
    def __init__(self):
        self.list_v=[]
        self.weight_=[]

    def appends(self,x,y,w):
        e=edge(x,y,w)
        self.list_v.append(e)
        self.weight_.append(w)

    def length(self):
        return len(self.list_v)
    
    def display_bag(self):
        for i in range(len(self.list_v)):
            self.list_v[i].display()


#Graph Class Data Structure containing the set of vertices and their adjacent edges
class DGraph: 
       
    def __init__(self,vert):
        self.vertices= [bag() for i in range(vert)]
        self.nov=vert
           
    def edge_formation(self,x,y,w):
        self.vertices[x].appends(x,y,w)
        
    def adjacent_vertices(self,x):
        return self.vertices[x]             
   
    def display(self):
        for k in range(self.nov):
            i=0
            adj_list=self.adjacent_vertices(k).list_bag()
            while i < len(adj_list):
                print("Edge: ",k,"---->",adj_list[i])
                i+=1 


if __name__=="__main__":
    
    #Note please give the path of the input text file here
    
    filename="4a.txt"
    #filename="4b.txt"
    file_=open(filename,"r")
    lines=file_.readlines()
    t_verts=int(lines[0].strip())    
    t_edges=int(lines[1].strip())
        
    #Graph Formation
    i=2
    gr=DGraph(t_verts)
        
    while i < len(lines):
        line=lines[i].strip()
        edges=line.split()
        gr.edge_formation(int(edges[0]),int(edges[1]),float(edges[2]))
        i+=1

    #Now we start with -------------Dijakstra Algorithm---------------
    
    #Shortest Path Data Structure
    source=[edge(-1,-1,1000) for k in range(t_verts)]
    dist_=[0 for k in range(t_verts)]

    dist_v=[10000 for k in range(t_verts)]#Distances which are to be compared for every relaxation
    #Note that instead of infinity 10000 is being used 
    dist_v[0]=0 # Note 0 is the source from where we are starting 
    marked=[0 for k in range(t_verts)]
    # We are marking the verteices as 0
    ipq_=ipq(t_verts) # Indexed Priority Queue for keeping the minimum value on the top
    
    #First we put the bag of adjacent vertices of vertex 0 i.e. the starting Point
    
    bag_v=gr.adjacent_vertices(0) # first getting the bag of edges of the vertex 0
    
    for i in range(len(bag_v.list_v)): # go through the whole lists in the bag
        # Relax all the adjacent Points
        if(bag_v.weight_[i]+dist_v[0] < dist_v[bag_v.list_v[i].other_point()]):
            dist_v[bag_v.list_v[i].other_point()]=bag_v.weight_[i]+dist_v[0]           
            bag_v.list_v[i].weigh=dist_v[bag_v.list_v[i].other_point()]           
            if ipq_.index_[bag_v.list_v[i].other_point()]==-1:
                ipq_.insert_key(bag_v.list_v[i],bag_v.list_v[i].other_point())
            else:
                ipq_.decrease_key(bag_v.list_v[i],bag_v.list_v[i].other_point())
        # note the above code ids relaxation code 
        # where we are relaxing edges i.e. the wieight of the edge + Dist[source vertex] < distance pointing vertex then change
        #Change the edge in the index of the prioirty queue corresponding to the pointing vertex
        # maintain then finalised distance to that vertex in the dist_v list
    
    # Using the prioirty queue Min heap we will be going to all vertices in the ascending order 
        
    prev=0
    # loop till the priority queue empty
    #Priority queue is holding the pointing to edges corresponding to the shortest path towards that point 
    while ipq_.size() > 0 :
        # we are deleting the minimum 
        minim=ipq_.delete_min()        
        point=minim.p
        source[point]=minim.e       
        dist_[point]=dist_v[point] # updating its distance in the list
        bag_v=gr.adjacent_vertices(point) # getting the adjacent vertices

        for i in range(len(bag_v.list_v)): # performing relaxation for all 
            # Relax all the adjacent Points
                if(bag_v.weight_[i]+dist_v[point] < dist_v[bag_v.list_v[i].other_point()]):
                    dist_v[bag_v.list_v[i].other_point()]=bag_v.weight_[i]+dist_v[point]
                    bag_v.list_v[i].weigh=dist_v[bag_v.list_v[i].other_point()]
                    if ipq_.index_[bag_v.list_v[i].other_point()]==-1:
                        ipq_.insert_key(bag_v.list_v[i],bag_v.list_v[i].other_point())     
                    else:
                        ipq_.decrease_key(bag_v.list_v[i],bag_v.list_v[i].other_point())
                        
        
        
        
    
    #Display of Shortest Path in the whole graph from the zero vertex
    # here the last edges pointing to 1-7 are displayed and teh distance dispalyed is final distance to that point/vertex from 0
    print("Shortest Path Results- From --- Vertex---Total Dist")
    m=1
    while m < t_verts:
        source[m].display()
        m+=1
    print("Note : Second Column are the vertices for which origin of the edge is in first column and total distance from source is in third column")
    

