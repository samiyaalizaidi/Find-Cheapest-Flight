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

def AddEdges(G, edges):
    for j in G:
        lst = []
        for k in range(len(edges)):
            if j == edges[k][0]:
                lst.append(edges[k])
        G[j] = lst
    return(G)

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


# # converts the list into a proper output.
# def format_function(string):
#     length = len(string)
#     answer = f"{str(length)} possible routes found. \n \n"
#     num = 1
#     for text in string:
#         answer = answer + str(num) + '. ' + text + "\n"
#         num += 1
#     return answer
# # print(format_function(x))

# # Takes information from the 'Enter' button and uses it to generate output.
# def ActualWork(start, end, graph):
#     try:
#         start = start.capitalize()
#         end = end.capitalize()

#         # returns error if a node (city) is not in the database.

#         if start not in Graph or end not in Graph:
#             label["foreground"] = "#E61F0E" # sets the text color to red
#             label['text'] = "Oops! No Current Flight Available."

#         elif start == end:
#             label["foreground"] = "#E61F0E" # sets the text color to red
#             label['text'] = "Invalid Information."

#         else:
#             # gives the output in the form of a list
#             x = SortAndPrint(graph, start, end)
#             # assigns the formatted string to the GUI output
#             label["foreground"] = "#020C01"
#             label['text'] = format_function(x)

#     # this will give an output if there is an error / program crashes
#     except:
#         label["foreground"] = "#E61F0E" # sets the text color to red
#         label["text"] = "There was a problem retrieving that information. Please try again later."

# # 
# Helper functions for the shortest path code ends here
# 

# Making the parent display window
window = Tk() # Initializes the GUI
window.configure(background="#80c1ff") # gives sky blue background color
window.title("SHH Travelling Agency") # label
window.geometry("1200x1000") # sets the size of the window  

# making functions for the new windows

# 1. Finding Cheapest Flights
def Finding_Flights():
    window = Tk() # Initializes the GUI
    window.configure(background="#80c1ff") # gives sky blue background color
    window.title("Get Plane Tickets") # label
    window.geometry("1200x1000") # sets the size of the window 
    global Graph
    # converts the list into a proper output.
    def format_function(string):
        length = len(string)
        answer = f"{str(length)} possible routes found. \n \n"
        num = 1
        for text in string:
            answer = answer + str(num) + '. ' + text + "\n"
            num += 1
        return answer
    # print(format_function(x))

    # Takes information from the 'Enter' button and uses it to generate output.
    def ActualWork(start, end, graph):
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
    
    button = Button(frame, text="ENTER", font=("Times New Roman", 20, 'bold'), command=lambda: ActualWork(entry_from.get(), entry_to.get(), Graph), bg='#FF5733')
    button.place(relwidth=0.2, relheight=1, relx=0.8) # to press the button ---> processes the information entered in the text boxes.

    lower_frame = Frame(window, bg='#80c1ff', bd=10)
    lower_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.6, anchor='n') # route will appear here

    label = Label(lower_frame, bg='#80c1ff', font=("Times New Roman", 20, 'bold'), anchor='n', justify='left')
    label.place(relx=0, rely=0) # for the route

    window.mainloop() # terminates the execution of gui 

# 2. Adding flights to the database
def Add_New_Flights():
    window = Tk() # Initializes the GUI
    window.configure(background="#80c1ff") # gives sky blue background color
    window.title("Add New Flights") # label
    window.geometry("1200x1000") # sets the size of the window 
    
    # Making frames for the window
    upper_frame = Frame(window, bg='#80c1ff', bd=10)
    upper_frame.place(relx=0.5, rely=0.02, relwidth=0.75, relheight=0.15, anchor='n') # for title

    text = Label(upper_frame, text="SHH Travelling Agency and Co.", font=("Times New Roman", 40, "bold"), bg='#80c1ff')
    text.place(relx=0.15) # Project title comes here 
    
# 3. Deleting flights from the database
def Delete_Flights():
    window = Tk() # Initializes the GUI
    window.configure(background="#80c1ff") # gives sky blue background color
    window.title("Delete Flights") # label
    window.geometry("1200x1000") # sets the size of the window  

    # Making frames for the window
    upper_frame = Frame(window, bg='#80c1ff', bd=10)
    upper_frame.place(relx=0.5, rely=0.02, relwidth=0.75, relheight=0.15, anchor='n') # for title

    text = Label(upper_frame, text="SHH Travelling Agency and Co.", font=("Times New Roman", 40, "bold"), bg='#80c1ff')
    text.place(relx=0.15) # Project title comes here

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

window.mainloop() # terminates the execution of GUI