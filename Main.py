from tkinter import *
from tkinter import filedialog 
from tkinter import scrolledtext
from string import punctuation
from collections import OrderedDict 
import numpy as np
import matplotlib.pyplot as plt
import os

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
        self.skip_words = ["", " ", "	", "ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"]

        self.title("Text Analyzer")
        self.geometry("700x500")

        self.label_file_explorer = Label(self,  
                            text = "Text Analyzer", 
                            width = 100, height = 4,  
                            fg = "blue") 
        self.label_file_stats = Label(self, text = "Choose a file to display relevant statistics")
   
        self.button_browse = Button(self, text = "Browse Files", command = self.browseFiles, width=20)  
        self.button_exit = Button(self, text = "Exit", command = exit, width=20)
        self.button_show_histogram = Button(self, text = "Plot Word Frequencies", command = self.showHistogram, width=20)
        self.button_update_file = Button(self, text = "Refresh Stats", command = self.analyze, width=20)
        self.button_keyword_file = Button(self, text = "Browse Keyword File", command = self.browseKeywordFiles, width=20)
        self.button_displayKeywordSentences = Button(self, text = "Keyword Sentences", command = self.displayKeywordSentences, width=20)

        self.label_file_explorer.grid(column = 0, row = 1, columnspan = 3)
        self.label_file_stats.grid(column = 0, row = 2, columnspan = 2, rowspan = 3)
        self.button_browse.grid(column = 2, row = 3)
        self.button_update_file.grid(column = 2, row = 4)
        self.button_show_histogram.grid(column = 2, row = 5)
        self.button_keyword_file.grid(column = 2, row = 6)
        self.button_displayKeywordSentences.grid(column = 2, row = 7)
        self.button_exit.grid(column = 2, row = 8)

    def browseFiles(self): 
        """File explorer to choose file and analyze"""

        temp_path = filedialog.askopenfilename(title = "Select a File", filetypes = (("Text Files", "*.txt"), ("All Files", "*"))) 
        if temp_path:
            self.file_path = temp_path
            self.label_file_explorer.configure(text = "File: " + self.file_path)
            self.analyze()

    def browseKeywordFiles(self): 
        """File explorer to choose keyword file"""

        temp_path = filedialog.askopenfilename(title = "Select a File", filetypes = (("Text Files", "*.txt"), ("All Files", "*"))) 
        if temp_path:
            self.keywords_file = temp_path
            self.label_file_explorer.configure(text = self.keywords_file)
 
    def analyze(self):
        """Analyzes the file and computes the required statistics"""

        if self.file_path:
            self.word_dictionary = dict()
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
            text.close()
            self.printNoOfLinesSentences()
            self.printLeastMostFrequency()
            self.printFrequency()

    def printFrequency(self):
        """Displays the necessary statistics in a new window"""

        if self.file_path:
            text_area = scrolledtext.ScrolledText(self, 
                                width = 40,  
                                height = 8,  
                                font = ("Times New Roman", 11))
            text_area_title = "Word frequencies are:\n"
            text_area.grid(column = 0, row = 14, columnspan = 2, rowspan = 12, sticky=W+N, padx=10, pady=10)
            text_area.insert(INSERT, text_area_title)
            for keys, values in self.word_dictionary.items(): 
                print_line = str(keys) + " : " + str(values) + "\n"
                # text_area.grid(column = 0, row = 14, columnspan = 2, rowspan = 12, sticky=W+N, padx=10, pady=10)
                text_area.insert(INSERT,print_line) 
            text_area.configure(state ='disabled')

    def printLeastMostFrequency(self):
        """Displays the necessary statistics in a new window"""

        if self.file_path:
            text_area = scrolledtext.ScrolledText(self, 
                                width = 40,  
                                height = 8,  
                                font = ("Times New Roman", 11))

            itemMaxValue = max(self.word_dictionary.items(), key=lambda x: x[1])
            print_line = "Word(s) with max frequency (" + str(itemMaxValue[1]) + ") is/are: \n"
            text_area.grid(column = 0, row = 5, columnspan = 2, rowspan = 7, sticky=W+N, padx=10, pady=10)
            text_area.insert(INSERT,print_line)

            for key, value in self.word_dictionary.items():
                if value == itemMaxValue[1]:
                    print_line = str(key) + "\n"
                    # text_area.grid(column = 0, pady = 10, padx = 10)
                    text_area.insert(INSERT,print_line)

            itemMinValue = min(self.word_dictionary.items(), key=lambda x: x[1])
            print_line = "Word(s) with min frequency (" + str(itemMinValue[1]) + ") is/are: \n"
            # text_area.grid(column = 0, pady = 10, padx = 10)
            text_area.insert(INSERT,print_line)
            
            for key, value in self.word_dictionary.items():
                if value == itemMinValue[1]:
                    print_line = str(key) + "\n"
                    # text_area.grid(column = 0, pady = 10, padx = 10)
                    text_area.insert(INSERT,print_line)

            text_area.configure(state ='disabled')

    def printNoOfLinesSentences(self):
        """Displays the necessary statistics in the main window"""

        if self.file_path:
            text = open(self.file_path, "r") 
            Content = text.read() 
            CoList = Content.split("\n") 
            SentenceCounter = 0
            Counter = 0
            for i in CoList: 
                if i: 
                    Counter += 1
            
            SentenceCounter += Content.count('.') + Content.count('!') + Content.count('?') 

            SentenceCounter = max(SentenceCounter, Counter)
            word_counter = len(Content.split())
            file_stats = "Num Words: " + str(word_counter) + "\nNum Sentences: " + str(SentenceCounter) + "\nNum Newlines: " + str(Counter)
            self.label_file_stats.configure(text = file_stats)

    def showHistogram(self):
        if(self.file_path):
            my_colors = [(x/(len(self.word_dictionary)+20), x/(len(self.word_dictionary)+100), 0.75) for x in range(len(self.word_dictionary))]
            plt.bar(list(self.word_dictionary.keys()), self.word_dictionary.values(),color=my_colors, width=0.5)
            plt.title('Word Frequency')
            plt.xlabel('Words')
            plt.ylabel('Frequency')
            plt.show()
        else:
            self.label_file_explorer.configure(text="Please select the file")

    def displayKeywordSentences(self):
        if self.keywords_file and self.file_path:
            k = open(self.keywords_file, "r")
            keywords = []
            for keyword in k:
                keyword = keyword.strip('\n')
                keywords =  keywords + [keyword]
            k.close()

            f = open(self.file_path, "r")
            temp_f = open("temp_keywords.txt", "w")

            for line in f:
                buffer = line.replace("\n", "")
                buffer = line.replace("\t", "")
                buffer = buffer.replace(". ", ".\n")

                temp_f.write(buffer)

            f.close()
            temp_f.close()

            temp_f = open("temp_keywords.txt", "r")

            containskeyword = False

            newWindow = Toplevel(self)

            text_area = scrolledtext.ScrolledText(newWindow, 
                                width = 100,  
                                height = 30,  
                                font = ("Times New Roman", 11))
            text_area.grid(column = 0, pady = 10, padx = 10)
            text_area.insert(INSERT, "The sentences containing keywords are:\n")

            for sentence in temp_f:
                for keyword in keywords:
                    if keyword in sentence:
                        containskeyword = True
                
                if containskeyword == True:
                    containskeyword = False
                    #print sentence to window
                    sentence = sentence + '\n'
                    text_area.insert(INSERT,sentence)

            temp_f.close()
            os.remove("temp_keywords.txt")

            text_area.configure(state ='disabled')
            newWindow.mainloop()

        else:
            self.label_file_explorer.configure(text="Please select both the files")



if __name__ == "__main__":
    app = App()
    app.mainloop()