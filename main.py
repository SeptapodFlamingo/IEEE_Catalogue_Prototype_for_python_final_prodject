from IEEECatSearchGUI import *
from search import *
import csv

def main():
    
    appl = QApplication([])
    window = Search()
    window.show()
    appl.exec()
 


 
    
    
    
    
if __name__ == '__main__':
    main()



"""

Data validation for input coming from the keyboard.
Exception handling must be present to deal with runtime errors.
OOP best practices must be implemented 
        (Separating code to classes, data hiding, inheritance - lab 10, test 10, and lab 12 are great examples).
Proper documentation.
Using descriptive variable names, class names, and file names.
Docstrings for all functions.
Type hinting for all function headers.
Public GitHub link submitted with all project files placed/merged into the main/master branch. 
    The project files could range from:
            python files, images, documents, images, sound files, text files, binary files, executable files, etc. 
            (generally anything that is needed for the application to work) 
            - Delete any files that are not used in the project or any extra branches you were working with -
            all code should be placed in the main/master branch.
"""