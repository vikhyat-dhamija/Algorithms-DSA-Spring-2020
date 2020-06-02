from time import time

#Problem is solved by a strategy which is a multiple source Dijkstra we need to apply and find the maximum path distance from one
#vertex to another which will be the diameter
#Let us firtst create a Data Structure for edge
class edge:
    #Note that here we construct the edge data structure with the source point , 
    def __init__(self,x,y,w):
        self.source=x
        self.dest=y
        self.weight=w
    # for getting the source point
    def source_point(self):
        return self.source
    # for getting the destination point
    def dest_point(self):
        return self.dest
    # for displaying the edge
    def display(self):
        print(self.source,"---->",self.dest,"-----",self.weight)
    #for comparison of both edges as it will be required in the indexed prioirty queue 
    def compare(self,e):
        if(e.weight > self.weight) :
            return 1
        elif e.weight < self.weight :
            return -1
        else:
            return 0

#Data Structure for the bag of edges that correspond to the adjacency list of each vertex basically it is the list of edges or adjacent vertices 
#with respect to one vertex
class bag:
    def __init__(self,vertices):
        self.edge_list=[]
        self.weight_=[]
#Note in my style of implementation weight is again created separately for each edge 
#Reason being that further in the priority queue where minimum is at the top then that minimum is based on the distance
#And that distance will be updated in the weight field of the edge structure so as to compare
# And moving the edges up and down in the structure
#That is why weight for each adjacent edge is also kept separately
        
    # adding edge in the bag of corresponding vertex
    def add_edge(self,s,d,w):
        self.edge_list.append(edge(s,d,w))
        self.weight_.append(w)
    # weight is also appended separately    

    
# Data structure for Graph
class Graph:
    #for initialisation with number of bags corresponding to each vertices
    def __init__(self,vertices):
        self.vertices= [bag(vertices) for i in range(vertices)]
        self.total_v=vertices

    def add_edge(self,s,d,w):
        self.vertices[s].add_edge(s,d,w)



#Indexed priority queue for Dijakstra implementation based on the binary heap for Log operations
class ipqueue:

    #for indexed priority queues we need the edges list which will behave as min heap with minimum above and the 2*i and 2*i+1 as children and so on
    #Then with indexed queue is that we need a list storing the indexes of vertices so that as we pass on the vertex like 0,1,2 we may get the index in the list of heap
    #As heap is a structure which modifies the position of elements/rearranges so as to maintain a priority here the minimum heap
    
    def __init__(self,vertices): # as we have to create the list as per the number of vertices as in dijkstra we will be working vertex by vertex so
        # we have to decrease key and insertion with respect to index and delete min operation
        self.vertices=[-1 for i in range(vertices)]
        #the vertices list is for the vertex  particular entry in the list of edges maintained in the prioity queue corresponds to  
        self.lists=[edge(-1,-1,1000) for i in range(vertices)]#Note seeing the datsets provided I have taken 1000 as the infinity or other numbers could have been chosen
        self.index=[-1 for k in range(vertices)] # index it is miply for look up that is we pass the vertex and we get the index in the lists of the priority queue
        self.n=-1 # The intial counter for the list of heap here named lists

    # We have to implement three operations delete minimum , insertion at a particular index and decreasing i.e. we can say some kind of changing at a particular index and then rearranging to maintain the priority
    # But for that we need the swim up and swim down/sink operation
    # swim up is needed as we insert into the last of the list and then compare with the parent that i am not more and then further till the top of the heap
    # similar is for when we decrease the key then it has to swim up in order to maintain the priority of the minimum at the top

    # That we indicate that we have to move the element at particular index upwards
    # Note that while in swim up we are just considering comparison with the parent 

    def swim_up(self,index):
        if index <= 0:
            parent= -1
        else:
            parent=int((index-1)/2)
        
        while(parent >= 0):
            
            if self.lists[parent].weight > self.lists[index].weight:
                self.swap(parent,index)
            
            # we change the index and the parent

            if parent <= 0:
                parent= -1
            else:
                parent=int((parent-1)/2)

            if index <=0:
                index=-1
            else:
                index=int((index-1)/2)

    #swim down operation
    def swim_down(self):
        # checking whether the ist is having certain elements 
        # This operation is useful when we ahve to delete i.e we remove the element from the top i.e. the minimum
        #put the last element and then we swim dowmn as to make the priority queue arrangement
        
        if(self.n >= 0):
            i=0
            # here we loop through till we reach the just upper level to the lower in order to compare with children
            while(i <= int((self.n-1)/2)):
                #Here we find the the smaller of the two children                
                #This is to check the boundary condition if no children is there and we reach the boundary because it is a balanced tree 
                # so one children condition will occur at the boundary
                if((2*i+2)<= self.n):
                    j=self.less_find(2*i+1,2*i+2)
                else:
                    j=2*i+1    
                #then weight comparison between the parent and the lesser child and if the parent is smaller than the children j then swap it             
                if(self.lists[i].weight > self.lists[j].weight):
                    self.swap(i,j)
                i=j
    
    #Swapping and less find functions 
    def swap(self,i,j):
        # First swapping the list elements
        temp=self.lists[i] 
        self.lists[i]=self.lists[j]  
        self.lists[j]=temp
        
        # Swapping the vertex to which this edges belongs
        temp=self.vertices[i] 
        self.vertices[i]=self.vertices[j]  
        self.vertices[j]=temp
    
        # Change the index of the vertices as the edges position has changed
        self.index[self.vertices[j]]=j
        self.index[self.vertices[i]]=i
         
    #less find function
    def less_find(self,pos1, pos2):
        if self.lists[pos1].weight < self.lists[pos2].weight:
            return pos1
        else:
            return pos2

    #Insert , decrease key and the delete min operations
    def insert_(self,ed, index_):
        self.n+=1 # first we incresae as we have initialised with -1 so always increase first and then put the edge in it
        self.lists[self.n]=ed # put the edge at the last
        self.vertices[self.n]=index_ #put the index in the listof vertices because index corresponds to the vertex
        self.index[index_]=self.n #put the index of the latest vertex corresponding here as index_into the index list    
        self.swim_up(self.n) # Then swim up
        #swim up will take care of movements of all vertices , lists and other index list structure

    #Decrease key just replace the key at particular index and then swim up to maintain heap
    def decrease_weight(self,ed,index_):
        #First we check that index is within bounds of the list
        if(self.n >= self.index[index_]) :
            self.lists[self.index[index_]]=ed
            self.swim_up(self.index[index_])
        # Note here I am putting the new value of e i.e will be having the lesser weight value and leaving the existing object for garbage collection
        #Not manipulating the to , from and the weight of existing object structure at particular edge

    #Last function and important one i.e. to delete the minimum
    def delete_min(self):
        #That onle one elemnet is there we need not do any putting of last element and then sink down
        if self.n==0:
            min=self.lists[self.n]
            self.lists[self.n]=edge(-1,-1,-1) 
            self.vertices[self.n]=-1
            self.index[self.vertices[self.n]]=-1
            self.n-=1
            return min
        
        elif(self.n > 0):
            min=self.lists[0]           
            self.lists[0]=self.lists[self.n]
            self.vertices[0]=self.vertices[self.n]
            self.index[self.vertices[0]]=0
            self.lists[self.n]=edge(-1,-1,1000)
            self.vertices[self.n]=-1
            
            self.n=self.n-1
            self.swim_down()           
            return min

    #Check whether any particular vertex is empty or not for this we check the index of that vertex that its value is -1 then index does not exist and vertex does not exist 
    def v_empty(self,vertex):
        if self.index[vertex]==-1:
            return 1 # return 1 in case of empty
        else:
            return 0 # return 0 in case of filled
    
    #to check whether the indexed priority queue has become empty or not
    def size(self):
        return (self.n+1)

#This function is for relaxing all the edges of the vertex passed
def relax_vertex(source,edge_to,dist,bag,ipqueue):    
    
    for i in range(len(bag.edge_list)):

        if(bag.weight_[i] + dist[source] < dist[bag.edge_list[i].dest_point()]):
            dist[bag.edge_list[i].dest_point()]=bag.weight_[i] + dist[source]
            bag.edge_list[i].weight=dist[bag.edge_list[i].dest_point()]                   
            if ipqueue.index[bag.edge_list[i].dest_point()]==-1:
                ipqueue.insert_(bag.edge_list[i],bag.edge_list[i].dest_point())
            else:
                ipqueue.decrease_weight(bag.edge_list[i],bag.edge_list[i].dest_point())


#Then let us go to actual implementation of Dijkstra which will be multi source
if __name__=="__main__":
    
    #File reading here
    files="ds_1.txt"
    file_=open(files,"r")
    lines=file_.readlines()
    nov=int(lines[0].strip())   #Number of vertices 
    noe=int(lines[1].strip())   #Number of edges
        
    #Graph Formation 0 , 1 index we have alreday captured for number of vertices and edges
    i=2
    graphs=Graph(nov)#Graph structure is being created

    #the file is being read and each edge is added in the graph    
    while i < len(lines):
        line=lines[i].strip()
        edges=line.split()
        graphs.add_edge(int(edges[0]),int(edges[1]),float(edges[2]))
        i+=1

#Multiple sources Dijkstra
t0=time()
#note that as we need to calculate the diameter which is the maximum shortest path so we have kept the edge as a data structure for path 
#from one vertex to another with maximum shortest path
max_path=edge(-1,-1,-1000)

#The first loop for the all vertices as we need to find the shortest p
for svt in range(nov): 

    #Shortest Path Data Structure
    edge_to=[edge(-1,-1,1000) for k in range(nov)]#these are the edges that lead to each vertex in the shortest path towards them
    dist=[10000 for p in range(nov)]#Distances to each vertex 10000 being used as an initial distance of infinity for Dijkstra
    
    dist[svt]=0 # Source vertex distance is set only to 0 
    ipqueues=ipqueue(nov) 
    
   
    _bag=graphs.vertices[svt] # Bag of adjacent vertices of source from where we are starting
    
    #relax edges of the source vertex
    relax_vertex(svt,edge_to,dist,_bag,ipqueues)
    
    #While size of the priority queue is greater than 0
    # I here want to emphasize that considering the dataset has positive weights other wise it will become bellman ford 
    
    while ipqueues.size() > 0 :
        
        #Minimum edge is selected 
        minimum=ipqueues.delete_min() 
        point=minimum.dest
        edge_to[point]=minimum
        
        
        #Additional code for calculation of the max_path with edge structure is used for putting the maximum value with distance in its weight        
        if dist[point] > max_path.weight and minimum.weight != 1000:
            max_path.dest=minimum.dest
            max_path.source=svt
            max_path.weight=dist[point]
        
        _bag=graphs.vertices[point] # getting the adjacent vertices

        relax_vertex(point,edge_to,dist,_bag,ipqueues)
                        
t1=time()

print("The diameter is a path between the points-------with distance value : ")
max_path.display()  
print("The time taken for the algorithm to execute is : ",(t1-t0)*1000," miliseconds")

    
