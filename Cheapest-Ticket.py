#helper functions
def GetNeighbours(G,node):
    lst = []
    for i in G:
        if i == node:
            for j in G[i]:
                lst.append(j[1])
            return(lst)

def Is_empty(queue):
    if len(queue) == 0:
        return(True)
    else:
        return(False)

def enqueue(a,b):
    a.append(b)
    return(a)

def dequeue(a):
    x = a[0]
    del a[0]
    return(x)

def is_empty(queue):
    if len(queue) == 0:
        return(True)
    else:
        return(False)


def AddVertex(graph, label):
  graph[label] = []
  return(graph)

def AddEdges(G, edges):
    for j in G:
        lst = []
        for k in range(len(edges)):
            if j == edges[k][0]:
                lst.append(edges[k])
        G[j] = lst
    return(G)

def Add_new_vertex(Graph,node):
    if node not in Graph:
        Graph[node] = []
        return(Graph)

def del_edge(Graph,node1,infom):
    pass
    if node1 in Graph:
        for i in Graph[node1]:
            if i == infom:
                Graph[node1].remove(i)
                return(Graph)
            
def update(Graph,node1,ifo,bifo):
    for i in Graph[node1]:
        if i == ifo:
            Graph[node1].remove(i)
            Graph[node1].append(bifo)
            return(Graph)

#file loader
def fileName():
  f = open("Dataset.txt", "r")
  x = f.read()
  bst = []
  lst = []
  string = ""
  for i in x:
      if i == ",":
          bst.append(string)
          string = ""
      elif i == "\n":
          bst.append(string)
          lst.append(bst)
          string = ""
          bst = []
      else:
          string = string + i
  return(lst)

#Graphloader
def LoadGraph(fileName):
  G = {}
  x = fileName()
  for i in x:
    AddVertex(G,i[0])
  AddEdges(G,x)
  return(G)

Graph = LoadGraph(fileName)

#Add a flight
info = ["Bangkok","Sydney","Thai Airways","200"]
def Add_flight(Graph,info):
    Add_new_vertex(Graph,info[0])
    Add_new_vertex(Graph,info[1])
    x = fileName()
    binfo = [info[1],info[0],info[2],info[3]]
    x.append(info)
    x.append(binfo)
    AddEdges(Graph,x)
Add_flight(Graph,info)

#Delete a flight
infom = ["Bangkok","Sydney","Thai Airways","200"]
def delete_flight(Graph,infom):
    del_edge(Graph,infom[0],infom)
    binfom = [info[1],info[0],info[2],info[3]]
    del_edge(Graph,infom[1],binfom)
delete_flight(Graph,infom)

#Update a flight
ifo = ["Karachi","Dubai","Fly Dubai","175"]
bifo = ["Karachi","Dubai","Fly Dubai","200"]
def update_flight(Graph,ifo,bifo):
    update(Graph,ifo[0],ifo,bifo)
    ifom = [ifo[1],ifo[0],ifo[2],ifo[3]]
    bifom = [bifo[1],bifo[0],bifo[2],bifo[3]]
    update(Graph,ifo[1],ifom,bifom)
    print(Graph)
update_flight(Graph,ifo,bifo)

#Quicksort sorts the all possibel flights from lowest to highest
def merge(data,left,right):
    a = 0
    b = 0
    c = 0
    while a < len(left) and b < len(right):
        if left[a][-1] < right[b][-1]:
            data[c] = left[a]
            a = a + 1
            c = c + 1
        else:
            data[c] = right[b]
            b = b + 1
            c = c + 1
    while a < len(left):
      data[c] = left[a]
      a = a + 1
      c = c + 1
    while b < len(right):
      data[c] = right[b]
      b = b + 1
      c = c + 1

def mergeSort(data):
  if len(data) > 1:
    center = len(data) // 2
    left = data[:center]
    right = data[center:]
    mergeSort(left)
    mergeSort(right)
    merge(data,left,right)


#BFS Finds all the possible paths
Node1 = "Dubai"
Node2 = "Istanbul"
def BreadthFirstSearch(graph,start,end):
    path = []
    marked = []
    fst = []
    lst = []
    queue = []
    enqueue(queue,start)
    marked.append(start)
    while Is_empty(queue) == False:
        x = dequeue(queue)
        path.append(x)
        n = GetNeighbours(graph,x)
        for v in n:
            if v in marked:
                pass
            else:
                if v == end:
                    path.append(v)
                    s = path.copy()
                    fst.append(s)
                    path.pop()
                else:
                    enqueue(queue,v)
                    marked.append(v)
    for w in fst:
        if w not in lst:
            lst.append(w)
        else:
            pass
    return(lst)
r = BreadthFirstSearch(Graph,Node1,Node2)

#Cheapest Ticket Via All Possible Routes
qst = []
for q in r:
    dst = []
    for m in range(len(q)-1):
        gst = []
        for i in Graph[q[m]]:
            if i[1] == q[m+1]:
                gst.append(i)
        min = 10000
        for j in gst:
            h = int(j[-1])
            if h < min:
                min = h      
        for k in range(len(gst)):
            l = int(gst[k][-1])
            if l == min:
                dst.append(gst[k])
    qst.append(dst)

for r in qst:
    total = 0
    for t in r:
        total = total + int(t[-1])
    r.append(total)

mergeSort(qst)

xst = []
for p in qst:
    strings = ""
    for b in p[:-1]:
        if len(p[:-1]) > 1:
            strings = strings + str(b[0])+" to "+str(b[1])+" via "+str(b[2])+", then from "
        else:
            strings = strings + str(b[0])+" to "+str(b[1])+" via "+str(b[2])+", a direct flight"
    if len(p[:-1]) > 1:
        strings = strings [:-11] + " a connecting flight,"
    strings = strings + " at a price of $"+str(p[-1])+"."
    print(strings)


