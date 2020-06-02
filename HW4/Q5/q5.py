#Run DFS and BFS on the graph set NYC
#Edge Class Data Structure for holding the vertex and the weight

# Edge class Data structure for edges
class edge:
    
    def __init__(self,x,y,weigh):
        self.x=x
        self.y=y
        self.weigh=weigh

    def one_point(self):
        return self.x

    def other_point(self,v):
        if v==self.x :
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

#Bag Class Data Structure for holding the edges for each vertex it is the adjacency List holding the edges
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


#Graph Class Data Structure containing the set of vertices and their adjacent edges
class Graph: 
       
    def __init__(self,vert):
        self.vertices= [bag() for i in range(vert)]
        self.nov=vert
        self.marked= [0 for i in range(vert)]
        self.visited_count=0  

    def graph_reset(self):
        self.marked= [0 for i in range(self.nov)]
        self.visited_count=0  
    
    def edge_formation(self,x,y,w):
        self.vertices[x].appends(x,y,w)
        self.vertices[y].appends(x,y,w)
        
    def adjacent_vertices(self,x):
        return self.vertices[x]             
   
    def display(self):
        for k in range(self.nov):
            i=0
            adj_list=self.adjacent_vertices(k).list_bag()
            while i < len(adj_list):
                print("Edge: ",k,"---->",adj_list[i])
                i+=1 
    #for traversal over all connected components in the graph
    def dfs_traversal(self):
        for i in range(self.nov):
            if(self.marked[i]!=1):
                self.dfs(i) # Run dfs on the particular vertex reach other vertices from this source
    #for traversal over all connected components in the graph        
    def bfs_traversal(self):
        for i in range(self.nov):
            if(self.marked[i]!=1):
                self.dfs(i) # Run dfs on the particular vertex reach other vertices from this source

#Append and Pop of the list in python will be used to make it behave like the stack and queue
#DFS from particular source
    def dfs(self,source):
        
        parent=[] # For parents
        self.marked[source]=1 #source marked 1
        ad_list=self.adjacent_vertices(source).list_v # got the adjacency list
        parent.extend([source]*len(self.adjacent_vertices(source).list_v)) #parent of the other vertices 
        self.visited_count+=1 #for checking the visits here only one for starting

        while(len(ad_list) > 0):  #ad_list is a stack structured list used here

            next_parent=parent.pop() #popping of the next out of list of parent
            next=ad_list.pop().other_point(next_parent)#other point of the edge apart from parent 
            if self.marked[next]==0: # Visit
                self.marked[next]=1
                #print(next)
                self.visited_count+=1

                next_list=self.adjacent_vertices(next).list_v
                #appending in the stack list the other adjacent vertices
                for i in range(len(next_list)):
                    if self.marked[next_list[i].other_point(next)]!=1:
                        ad_list.append(next_list[i])
                        parent.append(next)
 
        
    #BFS from particular source
    # all things same as dfs but here we are using the queue
    def bfs(self,source):
        
        parent=[]
        self.marked[source]=1
        ad_list=self.adjacent_vertices(source).list_v
        parent.extend([source]*len(self.adjacent_vertices(source).list_v)) #parent of the other vertices 
        self.visited_count+=1

        while(len(ad_list) > 0):
                        
            next_parent=parent.pop(0)
            next=ad_list.pop(0).other_point(next_parent) # here pop 0 means we are accesing from the front so list is working as queue FIFO
            if self.marked[next]==0:
                self.marked[next]=1
                #print(next)
                self.visited_count+=1

                next_list=self.adjacent_vertices(next).list_v
                
                for i in range(len(next_list)):
                    if self.marked[next_list[i].other_point(next)]!=1:
                        ad_list.append(next_list[i])
                        parent.append(next)
        

#main function
if __name__=="__main__":

    #Note please give the path of the input text file here
    filename="NYC.txt"
    file_=open(filename,"r")
    lines=file_.readlines()
    t_verts=int(lines[0].strip())    
    t_edges=int(lines[1].strip())
    
    i=2
    #Formation of Graph in the form of adjacency list
    gr=Graph(t_verts)
    while i < len(lines):
        line=lines[i].strip()
        edges=line.split()  
        gr.edge_formation(int(edges[0]),int(edges[1]),float(edges[2]))
        i+=1
    
    print("-------------BFS Traversal------------------")
    gr.bfs_traversal()
    print("Total Visisted Count for BFS :",gr.visited_count)  

    gr.graph_reset()# resetting to make 0 all marked and visited count to 0
    
    print("-------------DFS Traversal------------------")
    gr.bfs_traversal()
    print("Total Visisted Count for DFS :",gr.visited_count)
