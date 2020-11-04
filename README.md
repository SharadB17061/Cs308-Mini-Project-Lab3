# Cs308-Mini-Project-Lab3
This repository contains the Code for Lab3 Mini Project.

# Group Members
A :  Akash Dakoor, b17032 <br />
B : Aditya Mantri, b17001 <br />
C : Arnav Prasad, b17036 <br />
D : Sharad Shukla, b17061 <br />
E : Anvay Shah, b17078 <br />

# Setup and Run
1. install python3 using 
``` sudo apt install python3 ```
2. install tkinter if not installed 
``` sudo apt-get install python3-tk ```
3. Clone the repository using git clone <br />
4. execute 
``` python3 Main.py ```

# Functions of Buttons
The GUI is split into two sides, the left shows relevant information regarding the selected file, and the right pane provides the user with 5 buttons with different functions:
1. **Browse Files** opens up a file browser in the current directory. On choosing a file, the app populates the left side with 
    - the count of words, sentences, newlines
    - the most and least frequent word(s)
    - the frequencies of all the words
2. **Refresh Stats** reads the file again and refreshes statistics
3. **Plot Frequencies** plots the frequencies of the words in a histogram
4. **Browse Keyword File** opens up a file browser in the current directory to choose the file with keywords.
5. **Keyword Sentences** opens up a new window and displays all the sentences from the main file that contain one or more keywords from the keyword file.

