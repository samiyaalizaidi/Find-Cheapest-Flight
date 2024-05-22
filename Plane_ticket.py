# GUI Starts Here
window = Tk()
window.configure(background="#80c1ff") # gives sky blue background color
window.title("Plane Tickets") # label
window.geometry("1200x1000") # size  1400x1000

# test graph
graph = {"Boston": [("Dubai", 600), ("Karachi", 1200), ("Sydney", 1500)], "Dubai": ["Karachi", 200],"Sydney": ["Karachi", 1200]}

def format_function(lst, start):
    answer = str(start)
    for i in lst:
        answer = answer + " --> " + i[1]
    return answer

def ActualWork(start, end, graph):
    # print(getShortestPath(graph, start, end))
    x = [("Boston", "Dubai"), ("Dubai", "Karachi")]
    label['text'] = format_function(x, start)


upper_frame = Frame(window, bg='#80c1ff', bd=10)
upper_frame.place(relx=0.5, rely=0.02, relwidth=0.75, relheight=0.15, anchor='n') # route will appear here

text = Label(upper_frame, text="Hammad Travelling Agency and Co.", font=("Times New Roman", 40, "bold"), bg='#80c1ff')
text.place(relx=0.1)

frame = Frame(window, bg='#80c1ff', bd=10)
frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.1, anchor='n')

text_from = Label(frame, text="From: ", font=("Times New Roman", 20, "bold"), bg='#80c1ff')
text_from.place(relx=0)

text_to = text = Label(frame, text="To: ", font=("Times New Roman", 20, "bold"), bg='#80c1ff')
text_to.place(relx=0.43)

entry_from = Entry(frame, font=40)
entry_from.place(relwidth=0.28, relheight=1, relx=0.1) # for text entry --> Destination

entry_to = Entry(frame, font=40)
entry_to.place(relwidth=0.28, relheight=1, relx=0.5) # for text entry --> Current Location

def both_inputs(start, end): # temp function
    print(f"From {start} to {end}")
  
button = Button(frame, text="ENTER", font=("Times New Roman",20, 'bold'), command=lambda: ActualWork(entry_from.get(), entry_to.get(), graph), bg='#FF5733')
button.place(relwidth=0.2, relheight=1, relx=0.8) # to press the button

lower_frame = Frame(window, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.6, anchor='n') # route will appear here

label = Label(lower_frame, bg='#80c1ff', font=40)
label.place(relx=0)

window.mainloop() # terminates the execution of gui 
 
