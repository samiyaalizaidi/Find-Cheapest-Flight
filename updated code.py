from tkinter import *

# Functions for the graph and shortest path

# graph helper functions
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

def Add_new_vertex(Graph,node):
    if node not in Graph:
        Graph[node] = []
        return(Graph)

def del_edge(Graph,node1,infom):
    if node1 in Graph:
        for i in Graph[node1]:
            if i == infom:
                Graph[node1].remove(i)
                return(Graph)

def AddEdges(G, edges):
    for j in G:
        lst = []
        for k in range(len(edges)):
            if j == edges[k][0]:
                lst.append(edges[k])
        G[j] = lst
    return(G)

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

#MergeSort sorts the all possible flights from lowest to highest
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

Graph = LoadGraph(fileName)

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

def SortAndPrint(graph, start, end):
    # BFS returns a list containing all possible routes
    r = BreadthFirstSearch(graph, start, end)
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

    # sorts the list in the order of cheapest to most expensive
    mergeSort(qst)

    # converts into proper sentences
    answer = []
    number_count = 1
    for p in qst:
        strings = ''
        for b in p[:-1]:
            if len(p[:-1]) > 1:
                strings = strings + str(b[0])+" to "+str(b[1])+" via "+str(b[2])+", \n"+  "then from "
            else:
                strings = strings + str(b[0])+" to "+str(b[1])+" via "+str(b[2])+", \n"+"a direct flight"

        if len(p[:-1]) > 1:
            strings = strings [:-11] +"\n" +" a connecting flight,"
        strings = strings + " at a price of $"+str(p[-1])+"."

        strings += "\n"
        number_count += 1
        answer.append(strings)
    print(answer)
    return answer

# Making the parent display window
window = Tk() # Initializes the GUI
window.configure(background="#80c1ff") # gives sky blue background color
window.title("SHH Travelling Agency") # label
window.geometry("1200x1000") # sets the size of the window  

# making functions for the new windows

# Helper function
def get_capital(word):
    word = word.split(" ")
    if len(word) > 1:
        ans = ''
        for i in range(len(word)):
            ans += word[i].capitalize() + " "
        return ans.rstrip()
    else:
        return word[0].capitalize()

# Finding_Flights() functions

# converts the list into a proper output.
def format_function(string):
    length = len(string)
    answer = f"{str(length)} possible route(s) found. \n \n"
    num = 1
    for text in string:
        answer = answer + str(num) + '. ' + text + "\n"
        num += 1
    return answer

def ActualWork(start, end, graph, label):
    try:
        start = start.capitalize()
        end = end.capitalize()

        # returns error if a node (city) is not in the database.

        if start not in Graph or end not in Graph:
            label["foreground"] = "#E61F0E" # sets the text color to red
            label['text'] = "Oops! No Current Flight Available."

        elif start == end:
            label["foreground"] = "#E61F0E" # sets the text color to red
            label['text'] = "Invalid Information."

        else:
            # gives the output in the form of a list
            x = SortAndPrint(graph, start, end)
            # assigns the formatted string to the GUI output
            label["foreground"] = "#020C01"
            label['text'] = format_function(x)

    # this will give an output if there is an error / program crashes
    except:
        label["foreground"] = "#E61F0E" # sets the text color to red
        label["text"] = "There was a problem retrieving that information. Please try again later."

# 1. Finding Cheapest Flights
def Finding_Flights():
    window = Tk() # Initializes the GUI
    window.configure(background="#80c1ff") # gives sky blue background color
    window.title("Get Plane Tickets") # label
    window.geometry("1200x1000") # sets the size of the window 
    global Graph

    upper_frame = Frame(window, bg='#80c1ff', bd=10)
    upper_frame.place(relx=0.5, rely=0.02, relwidth=0.75, relheight=0.15, anchor='n') # for title

    text = Label(upper_frame, text="SHH Travelling Agency and Co.", font=("Times New Roman", 40, "bold"), bg='#80c1ff')
    text.place(relx=0.17) # Project title comes here

    frame = Frame(window, bg='#80c1ff', bd=10)
    frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.1, anchor='n') # for text entry

    text_from = Label(frame, text="From: ", font=("Times New Roman", 22, "bold"), bg='#80c1ff')
    text_from.place(relx=0) # to add "From" label

    text_to = text = Label(frame, text="To: ", font=("Times New Roman", 22, "bold"), bg='#80c1ff')
    text_to.place(relx=0.43) # to add "To" label

    entry_from = Entry(frame, font=50)
    entry_from.place(relwidth=0.28, relheight=1, relx=0.1) # for text entry --> Destination

    entry_to = Entry(frame, font=50)
    entry_to.place(relwidth=0.28, relheight=1, relx=0.5) # for text entry --> Current Location
    
    lower_frame = Frame(window, bg='#80c1ff', bd=10)
    lower_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.6, anchor='n') # route will appear here

    label = Label(lower_frame, bg='#80c1ff', font=("Times New Roman", 20, 'bold'), anchor='n', justify='left')
    label.place(relx=0, rely=0) # for the route

    button = Button(frame, text="ENTER", font=("Times New Roman", 20, 'bold'), command=lambda: ActualWork(entry_from.get(), entry_to.get(), Graph, label), bg='#FF5733')
    button.place(relwidth=0.2, relheight=1, relx=0.8) # to press the button ---> processes the information entered in the text boxes.

    window.mainloop() # terminates the execution of gui 

# Add_New_Flights() functions
# input in this form:
# info = ["Bangkok","Sydney","Thai Airways","200"]

def Add_flight(Graph,info):
    Add_new_vertex(Graph,info[0])
    Add_new_vertex(Graph,info[1])
    x = fileName()
    binfo = [info[1],info[0],info[2],info[3]]
    x.append(info)
    x.append(binfo)
    AddEdges(Graph,x)
    # print(Graph)    

def New_Flights(graph, current, dest, airline, cost, errorMessage):
    try:
        current = get_capital(current)
        dest = get_capital(dest)
        airline = get_capital(airline)
        lst = [current, dest, airline, str(cost)]
        Add_flight(graph, lst)
    # this will give an output if program crashes        
    except:
        errorMessage['text'] = "There was a problem retrieving that information. Please try again later."

# 2. Adding flights to the database
def Add_New_Flights():
    window = Tk() # Initializes the GUI
    window.configure(background="#80c1ff") # gives sky blue background color
    window.title("Add New Flights") # label
    window.geometry("1200x1000") # sets the size of the window 
    
    global Graph

    # Making frames for the window
    upper_frame = Frame(window, bg='#80c1ff', bd=10)
    upper_frame.place(relx=0.5, rely=0.02, relwidth=0.75, relheight=0.15, anchor='n') # for title

    text = Label(upper_frame, text="SHH Travelling Agency and Co.", font=("Times New Roman", 40, "bold"), bg='#80c1ff')
    text.place(relx=0.15) # Project title comes here 

    midframe = Frame(window,  bg='#80c1ff', bd=10)
    midframe.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.1, anchor='n')

    guide = Label(midframe, text="Please enter the required information.", font=("Times New Roman", 20, "bold"), bg='#80c1ff')
    guide.place(relx=0.32)
    
    newFrame = Frame(window, bg='#80c1ff', bd=10)
    newFrame.place(relx=0.5, rely=0.30, relwidth=0.75, relheight=0.75, anchor='n')

    from_text = Label(newFrame, text="From: ", font=("Times New Roman", 22, "bold"), bg='#80c1ff')
    from_text.place(relx=0.01, relwidth=0.1)

    name_from = Entry(newFrame, font=40)
    name_from.place(relwidth=0.25, relheight=0.12, relx=0.13)

    to_text = Label(newFrame, text="To: ", font=("Times New Roman", 22, "bold"), bg='#80c1ff')
    to_text.place(relx=0.45, relwidth=0.1)

    name_to = Entry(newFrame, font=40)
    name_to.place(relwidth=0.25, relheight=0.12, relx=0.55)

    airline_text = Label(newFrame, text="Airline: ", font=("Times New Roman", 22, "bold"), bg='#80c1ff')
    airline_text.place(relx=0, relwidth=0.1, rely=0.3)

    name_airline = Entry(newFrame, font=40)
    name_airline.place(relwidth=0.25, relheight=0.12, relx=0.13, rely=0.3)

    price_text = Label(newFrame, text="Price: ", font=("Times New Roman", 22, "bold"), bg='#80c1ff')
    price_text.place(relx=0.435, relwidth=0.1, rely=0.3)

    price = Entry(newFrame, font=40)
    price.place(relwidth=0.25, relheight=0.12, relx=0.55, rely=0.3)

    errorMessage = Label(newFrame, font=("Times New Roman", 15, "bold"), bg='#80c1ff', foreground="#F50000")
    errorMessage.place(relx=0.1, rely=0.68)

    update_button = Button(newFrame, text="Update", font=("Times New Roman", 20, "bold"),  bg='#C704B8', command=lambda: New_Flights(Graph, name_from.get(), name_to.get(), name_airline.get(), price.get(), errorMessage))
    update_button.place(relwidth=0.2, relheight=0.12, relx=0.37, rely=0.5)

# Delete_Flights() functions:

# input in this form:
# infom = ["Bangkok","Sydney","Thai Airways","200"]
def delete_flight(Graph,infom):
    del_edge(Graph,infom[0],infom)
    binfom = [infom[1],infom[0],infom[2],infom[3]]
    del_edge(Graph,infom[1],binfom)
    print(Graph)

def deletion(graph, current, dest, airline, cost, errorMessage):
    try:
        current = get_capital(current)
        dest = get_capital(dest)
        airline = get_capital(airline)

        # give an error if the flights dont exist
        print(graph)
        if current not in graph or dest not in graph:
            errorMessage['text'] = "No such flights found."
        else:
            lst = [current, dest, airline, str(cost)]
            delete_flight(graph, lst)

    # give an output if the program crashes
    except:
        errorMessage['text'] = "There was a problem. Please try again later."

# 3. Deleting flights from the database
def Delete_Flights():
    window = Tk() # Initializes the GUI
    window.configure(background="#80c1ff") # gives sky blue background color
    window.title("Delete Flights") # label
    window.geometry("1200x1000") # sets the size of the window  

    global Graph

    # Making frames for the window
    upper_frame = Frame(window, bg='#80c1ff', bd=10)
    upper_frame.place(relx=0.5, rely=0.02, relwidth=0.75, relheight=0.15, anchor='n') # for title

    text = Label(upper_frame, text="SHH Travelling Agency and Co.", font=("Times New Roman", 40, "bold"), bg='#80c1ff')
    text.place(relx=0.15) # Project title comes here

    midframe = Frame(window,  bg='#80c1ff', bd=10)
    midframe.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.1, anchor='n')

    guide = Label(midframe, text="Please enter the required information.", font=("Times New Roman", 20, "bold"), bg='#80c1ff')
    guide.place(relx=0.32)
    
    newFrame = Frame(window, bg='#80c1ff', bd=10)
    newFrame.place(relx=0.5, rely=0.30, relwidth=0.75, relheight=0.75, anchor='n')

    from_text = Label(newFrame, text="From: ", font=("Times New Roman", 22, "bold"), bg='#80c1ff')
    from_text.place(relx=0.01, relwidth=0.1)

    name_from = Entry(newFrame, font=40)
    name_from.place(relwidth=0.25, relheight=0.12, relx=0.13)

    to_text = Label(newFrame, text="To: ", font=("Times New Roman", 22, "bold"), bg='#80c1ff')
    to_text.place(relx=0.45, relwidth=0.1)

    name_to = Entry(newFrame, font=40)
    name_to.place(relwidth=0.25, relheight=0.12, relx=0.55)

    airline_text = Label(newFrame, text="Airline: ", font=("Times New Roman", 22, "bold"), bg='#80c1ff')
    airline_text.place(relx=0, relwidth=0.1, rely=0.3)

    name_airline = Entry(newFrame, font=40)
    name_airline.place(relwidth=0.25, relheight=0.12, relx=0.13, rely=0.3)

    price_text = Label(newFrame, text="Price: ", font=("Times New Roman", 22, "bold"), bg='#80c1ff')
    price_text.place(relx=0.435, relwidth=0.1, rely=0.3)

    price = Entry(newFrame, font=40)
    price.place(relwidth=0.25, relheight=0.12, relx=0.55, rely=0.3)

    errorMessage = Label(newFrame, font=("Times New Roman", 15, "bold"), bg='#80c1ff', foreground="#F50000")
    errorMessage.place(relx=0.1, rely=0.68)
    
    delete_button = Button(newFrame, text="Delete", font=("Times New Roman", 20, "bold"),  bg='#C704B8', command=lambda: deletion(Graph, name_from.get(), name_to.get(), name_airline.get(), price.get(), errorMessage))
    delete_button.place(relwidth=0.2, relheight=0.12, relx=0.37, rely=0.5)

# Update_Flights() functions
# input in this form:
# ifo = ["Karachi", "Dubai", "Fly Dubai", "175"]
# bifo = ["Karachi", "Dubai", "Fly Dubai", "200"]
# ifo --> old, bifo --> new
def update_flight(Graph,ifo,bifo):
    update(Graph,ifo[0],ifo,bifo)
    ifom = [ifo[1],ifo[0],ifo[2],ifo[3]]
    bifom = [bifo[1],bifo[0],bifo[2],bifo[3]]
    update(Graph,ifo[1],ifom,bifom)
    print(Graph)

def price_Update(graph, current, dest, airline, old, new, errorMessage):
    try:
        current = get_capital(current)
        dest = get_capital(dest)
        airline = get_capital(airline)

        # make sure the nodes exist in the graph
        print(graph)
        if current not in graph or dest not in graph:
            errorMessage['text'] = "No such flights found."
        else:
            old_list = [current, dest, airline, str(old)]
            new_list= [current, dest, airline, str(new)]
            update_flight(graph, old_list, new_list)

    # gives an output even if the program crashes.
    except:
        errorMessage['text'] = "There was a problem retrieving that data. Please try again later."

# 4. Updating flights from the database
def Update_Flights():
    window = Tk() # Initializes the GUI
    window.configure(background="#80c1ff") # gives sky blue background color
    window.title("Delete Flights") # label
    window.geometry("1200x1000") # sets the size of the window  

    global Graph

    # Making frames for the window
    upper_frame = Frame(window, bg='#80c1ff', bd=10)
    upper_frame.place(relx=0.5, rely=0.02, relwidth=0.75, relheight=0.15, anchor='n') # for title

    text = Label(upper_frame, text="SHH Travelling Agency and Co.", font=("Times New Roman", 40, "bold"), bg='#80c1ff')
    text.place(relx=0.15) # Project title comes here 

    midframe = Frame(window,  bg='#80c1ff', bd=10)
    midframe.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.1, anchor='n')

    guide = Label(midframe, text="Please enter the required information.", font=("Times New Roman", 20, "bold"), bg='#80c1ff')
    guide.place(relx=0.32)
    
    newFrame = Frame(window, bg='#80c1ff', bd=10)
    newFrame.place(relx=0.5, rely=0.30, relwidth=0.75, relheight=0.75, anchor='n')

    from_text = Label(newFrame, text="From: ", font=("Times New Roman", 22, "bold"), bg='#80c1ff')
    from_text.place(relx=0.01, relwidth=0.1)

    name_from = Entry(newFrame, font=40)
    name_from.place(relwidth=0.25, relheight=0.12, relx=0.13)

    to_text = Label(newFrame, text="To: ", font=("Times New Roman", 22, "bold"), bg='#80c1ff')
    to_text.place(relx=0.45, relwidth=0.1)

    name_to = Entry(newFrame, font=40)
    name_to.place(relwidth=0.25, relheight=0.12, relx=0.55)

    airline_text = Label(newFrame, text="Airline: ", font=("Times New Roman", 22, "bold"), bg='#80c1ff')
    airline_text.place(relx=0, relwidth=0.1, rely=0.3)

    name_airline = Entry(newFrame, font=40)
    name_airline.place(relwidth=0.25, relheight=0.12, relx=0.13, rely=0.3)

    priceOld_text = Label(newFrame, text="Old Price: ", font=("Times New Roman", 22, "bold"), bg='#80c1ff')
    priceOld_text.place(relx=0.40, relwidth=0.15, rely=0.3)

    priceOld = Entry(newFrame, font=40)
    priceOld.place(relwidth=0.25, relheight=0.12, relx=0.55, rely=0.3)

    priceNew_text =  Label(newFrame, text="New Price: ", font=("Times New Roman", 22, "bold"), bg='#80c1ff')
    priceNew_text.place(relx=0, relwidth=0.13, rely=0.6)

    priceNew = Entry(newFrame, font=40)
    priceNew.place(relwidth=0.25, relheight=0.12, relx=0.13, rely=0.6)

    errorMessage = Label(newFrame, font=("Times New Roman", 15, "bold"), bg='#80c1ff', foreground="#F50000")
    errorMessage.place(relx=0.1, rely=0.68)
    
    update_button = Button(newFrame, text="Update", font=("Times New Roman", 20, "bold"),  bg='#C704B8', command=lambda: price_Update(Graph, name_from.get(), name_to.get(), name_airline.get(), priceOld.get(), priceNew.get(), errorMessage))
    update_button.place(relwidth=0.2, relheight=0.12, relx=0.55, rely=0.6)

# Making Frames for the parent window
upper_frame = Frame(window, bg='#80c1ff', bd=10)
upper_frame.place(relx=0.5, rely=0.02, relwidth=0.75, relheight=0.15, anchor='n') # for title

text = Label(upper_frame, text="SHH Travelling Agency and Co.", font=("Times New Roman", 40, "bold"), bg='#80c1ff')
text.place(relx=0.15) # Project title comes here

frame = Frame(window, bg='#80c1ff', bd=10)
frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.1, anchor='n') # for text entry

message = Label(frame, text="Please select an action.", font=("Times New Roman", 20, "bold"), bg='#80c1ff')
message.place(relx=0.35)

button_frame = Frame(window, bg='#80c1ff', bd=10)
button_frame.place(relx=0.5, rely=0.30, relwidth=0.75, relheight=0.6, anchor='n')

getFlight = Button(button_frame, text="Find Flights!", bg='#FF5733', font=("Times New Roman", 20, "bold"), command=lambda: Finding_Flights())
getFlight.place(relwidth=0.2, relheight=0.1, relx=0.15)

addFlights = Button(button_frame, text="Add Flights", bg='#FF5733', font=("Times New Roman", 20, "bold"), command=lambda: Add_New_Flights())
addFlights.place(relwidth=0.2, relheight=0.1, relx=0.40)

removeFlights = Button(button_frame, text="Remove Flights", bg='#FF5733', font=("Times New Roman", 20, "bold"), command= lambda: Delete_Flights())
removeFlights.place(relwidth=0.23, relheight=0.1, relx=0.65)

updateFlights = Button(button_frame, text="Update Flights", bg='#FF5733', font=("Times New Roman", 20, "bold"), command=lambda: Update_Flights())
updateFlights.place(relwidth=0.23, relheight=0.1, relx=0.15, rely=0.2)
 
window.mainloop() # terminates the execution of GUI