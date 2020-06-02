#Cycle detection using the Depth First Search

# Here Bag is the list of vertices adjacent to particular list of vertices
#Way of representing the graph by Adjacency List representation 
#Please note that as the graph has to found to be cyclic / acyclic only vertices list has been stored not both vertex and weight
# as weight has no significance
class bag:
    def __init__(self):
        self.list_v=[]

    def appends(self,x):
        self.list_v.append(x)

    def length(self):
        return len(self.list_v)

    def list_bag(self):
        return self.list_v

    def display_bag(self):
        for i in range(len(self.list_v)):
            print(self.list_v[i])

#Graph is the data structure containing the required lists , variables and the set of vertices containing the bags corresponding to the vertices
class Graph: 

    is_cyclic=0 # Variable set when cycle detected
    #Here we initialise the data structures
    def __init__(self,vert):
        self.vertices= [bag() for i in range(vert)]
        self.c_marked=[0 for i in range(vert)]
        self.nov=vert
        self.is_cyclic=0
        
    #Edge formation as one undirected edge is a two way directed edge so one edge is added by adding the other vertex to bags of both vertex
    def edge_formation(self,x,y):
        self.vertices[x].appends(y)
        self.vertices[y].appends(x)

    # These are the adjacent vertices i.e. the bag of vertices when we want the bag of vertices to be returned
    def adjacent_vertices(self,x):
        return self.vertices[x]


    #This function is the Dfs function from one particular source with parent passed to it , so in check_cyclic function we have passed through all connected components in the graph
    def c_dfs(self,m,p):      
            adj=self.adjacent_vertices(m).list_bag()
            self.c_marked[m]=1
            j=0
            while (j < len(adj)):
                if self.c_marked[adj[j]] == 1 and p != adj[j] :
                    self.is_cyclic=1
                elif self.c_marked[adj[j]] != 1 :
                    self.c_dfs(adj[j],m)
                j+=1
        
    #here in order to check cycle we run the function till all vertices/nodes are visited and hence loop for visiting all vertices
    def check_cyclic(self):
        for k in range(self.nov):
            if(gr.c_marked[k] != 1):
                gr.c_dfs(k,-1)

    #This is for the graph display
    def display(self):
        for k in range(self.nov):
            i=0
            adj_list=self.adjacent_vertices(k).list_bag()
            while i < len(adj_list):
                print("Edge: ",k,"---->",adj_list[i])
                i+=1 


#main function
if __name__=="__main__":
    
    #Note please give the path of the input text file here
    #please note that it is assumed that the file contains in the format : Number of vertices , Edges , and then edges
    #otherwise the program may give error
    filename="dataset1_2.txt"
    file_=open(filename,"r")
    lines=file_.readlines()
    t_verts=int(lines[0].strip())    
    t_edges=int(lines[1].strip())
    
    i=2 #Starting Point of the lines in the file where edges are stored  
    
    #Formation of Graph
    gr=Graph(t_verts)
    while i < len(lines):
        line=lines[i].strip()
        edge=line.split()
        
        gr.edge_formation(int(edge[0]),int(edge[1]))# Note weights are not taken in consideration as we have to just detect the cycle
        
        i+=1
       
              
    #After we got the marked and parents in the graph Then we check using the check_cyclic function which runs the dfs again and do the 
    #Parent and the adjacent vertex comparison that the graph is cyclic
    gr.check_cyclic()

    #Above will set the is_cyclic global variable to 1 in case of the cycle is detected and print the result
    if(gr.is_cyclic==1):
        print("The Graph is cyclic")  
    else:
        print("The Graph is not cyclic/or acyclic")


         