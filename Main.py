from tkinter import *
   
# import filedialog module 
from tkinter import filedialog 
from tkinter import scrolledtext

filename = "/" 
# Create an empty dictionary 
d = dict() 
avoid = ["above", "across", "after", "against", "along", "among", "around", "at", "before", "behind", "below", "beneath", "beside", "between", "by", "down", "during", "for", "from", "in", "inside", "into", "near", "off", "on", "onto", "out of", "outside", "over", "through", "till", "to", "toward", "towards", "under", "underneath", "until", "up"]   
def getFrequency():
    text = open(filename, "r") 
 
# Loop through each line of the file 
    for line in text:  
        line = line.strip() 
    
        line = line.lower() 
    
        words = line.split(" ") 
    
        for word in words: 
            if word in d:  #TODO: add a condtion here to not consider words in avoid list here
                d[word] = d[word] + 1
            else: 
                d[word] = 1

# Function for opening the  
# file explorer window 
def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       
    # Change label contents 
       
def printFrequency():
    newWindow = Toplevel(window)
    Label(newWindow, 
          text = filename,
          width = 63, height = 4).pack()
    if filename == "/":
        label_test = Label(newWindow, 
                           text = "Open The file",
                           width = 63, height = 4).pack()

    else:
        for key in list(d.keys()): 
            print_line = key, ":", d[key] 
            label_test = Label(newWindow, 
                            text = print_line,
                            width = 63, height = 4).pack()
    

def analyseAndCollectData():
    browseFiles()                                                                           
# Create the root window 
window = Tk() 
   
# Set window title 
window.title('Text Analyser') 
   
# Set window size 
window.geometry("500x500") 
   
#Set window background color 
window.config(background = "white") 
   
# Create a File Explorer label 
label_file_explorer = Label(window,  
                            text = "File Explorer using Tkinter", 
                            width = 100, height = 4,  
                            fg = "blue") 
   
       
button_explore = Button(window,  
                        text = "Browse Files", 
                        command = browseFiles)  
   
button_exit = Button(window,  
                     text = "Exit", 
                     command = exit)  

button_get_frequency = Button(window, 
                             text = "Get Frequency", 
                             command = printFrequency)
   
# Grid method is chosen for placing 
# the widgets at respective positions  
# in a table like structure by 
# specifying rows and columns 
label_file_explorer.grid(column = 1, row = 1) 
   
button_explore.grid(column = 1, row = 3) 
   
button_exit.grid(column = 1,row = 4) 

button_get_frequency.grid(column = 1, row = 2)
   
# Let the window wait for any events 
window.mainloop() 