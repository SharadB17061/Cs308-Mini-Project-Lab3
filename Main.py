from tkinter import *
from tkinter import filedialog 
from tkinter import scrolledtext
from string import punctuation
from collections import OrderedDict 

class App(Tk):
    def __init__(self):
        super().__init__()
        self.file_path = ""
        self.keywords_file = ""
        self.num_words = 0
        self.num_sentences = 0
        self.num_newlines = 0
        self.word_dictionary = dict() 
        self.least_common = []
        self.most_common = []
        self.skip_words = ["", " ", "a", "an", "or", "but", "and", "above", "across", "after",        "against", "along", "among", "around", "at", "before", "behind", "below", "beneath", "beside", "between", "by", "down", "during", "for", "from", "in", "inside", "into", "near", "off", "on", "onto", "out of", "outside", "over", "through", "till", "to", "toward", "towards", "under", "underneath", "until", "up"]   

        self.title("Text Analyzer")
        self.geometry("500x500")
        self.config(background = "white")

        self.label_file_explorer = Label(self,  
                            text = "File Explorer using Tkinter", 
                            width = 100, height = 4,  
                            fg = "blue") 
   
        self.button_browse = Button(self, text = "Browse Files", command = self.browseFiles)  
        self.button_exit = Button(self, text = "Exit", command = exit)
        self.button_get_frequency = Button(self, text = "Get Frequency", command = self.printFrequency)
        self.button_update_file = Button(self, text = "Update File", command = self.analyze)
        self.label_file_explorer.grid(column = 1, row = 1)
        self.button_browse.grid(column = 1, row = 3)
        self.button_exit.grid(column = 1,row = 5)
        self.button_get_frequency.grid(column = 1, row = 2)
        self.button_update_file.grid(column = 1, row = 4)

    def browseFiles(self): 
        """File explorer to choose file and analze"""

        temp_path = filedialog.askopenfilename(title = "Select a File", filetypes = (("Text Files", "*.txt"), ("All Files", "*"))) 
        if temp_path:
            self.file_path = temp_path
            self.label_file_explorer.configure(text = self.file_path)
            self.analyze()
 
    def generateDictionary(self):
        """Analyzes the file and computes the required statistics

        Completed: computing frequency of (non article/preposition) words
        Todo: num_words, num_lines, num_sentences, most_common, least_common
        """
        if self.file_path:
            text = open(self.file_path, "r") 
            for line in text:  
                line = line.strip() 
                line = line.lower() 
                words = line.split(" ") 
                for word in words:
                    word = word.strip(punctuation) 
                    if word not in self.skip_words:
                        if word in self.word_dictionary:  
                            self.word_dictionary[word] += 1
                        else: 
                            self.word_dictionary[word] = 1
            self.word_dictionary = OrderedDict(sorted(self.word_dictionary.items()))                 

    def analyze(self):
        if self.file_path:
            self.word_dictionary = dict()
            self.generateDictionary() 

    def printFrequency(self):
        """Displays the necessary statistics in a new window"""

        newWindow = Toplevel(self)
        if self.file_path == "/":
            label_test = Label(newWindow, 
                            text = "Open The file",
                            width = 63, height = 4).pack()
        else:
            text_area = scrolledtext.ScrolledText(newWindow, 
                                width = 60,  
                                height = 14,  
                                font = ("Times New Roman", 15))
            for keys, values in self.word_dictionary.items(): 
                print_line = str(keys) + " : " + str(values) + "\n"
                text_area.grid(column = 0, pady = 10, padx = 10)
                text_area.insert(INSERT,print_line) 
            text_area.configure(state ='disabled')
        newWindow.mainloop()

if __name__ == "__main__":
    app = App()
    app.mainloop()