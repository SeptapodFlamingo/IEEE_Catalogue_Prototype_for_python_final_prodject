"""

File to take UI elements and give them function



"""

from PyQt6.QtWidgets import *
from IEEECatSearchGUI import *
import csv
from catallogue_searcher import *



class Search(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(lambda : self.search_event())
        self.pushButton_clear.clicked.connect(lambda : self.clear_values())
        
        self.radioButton_all.toggled.connect(lambda : self.unfinished_message())
             
        
    def unfinished_message(self):
        self.clear_radio()
        self.error_indicator.setText('Unfinished section, please re-select')
        #if self.radioButton_name.isChecked():
        self.radioButton_all.setChecked(False)

        
    def clear_values(self):
        self.clear_radio()
        self.clear_text()
        
    def clear_text(self):
        self.NameLineEdit.clear()
        self.QuantityLineEdit.clear()
        self.DescriptionLineEdit.clear()
        self.LabelLineEdit.clear()
        self.DrawerLineEdit.clear()
        self.ElseLineEdit.clear()
        
    def clear_radio(self):
        
        self.radioButton_name.setAutoExclusive(False);
        self.radioButton_name.setChecked(False);
        self.radioButton_name.setAutoExclusive(True);
        
        self.radioButton_quantity.setAutoExclusive(False);
        self.radioButton_quantity.setChecked(False);
        self.radioButton_quantity.setAutoExclusive(True);
        
        self.radioButton_description.setAutoExclusive(False);
        self.radioButton_description.setChecked(False);
        self.radioButton_description.setAutoExclusive(True);
        
        self.radioButton_location.setAutoExclusive(False);
        self.radioButton_location.setChecked(False);
        self.radioButton_location.setAutoExclusive(True);
        
        self.radioButton_all.setAutoExclusive(False);
        self.radioButton_all.setChecked(False);
        self.radioButton_all.setAutoExclusive(True);
        
        self.error_indicator.setText('Please fill out relevant values')
        
        
    
    def search_event(self):        
        #rb = self.sender()
        if self.radioButton_name.isChecked():
            selection = 'name'
            name = self.NameLineEdit.text().strip()
        
        elif self.radioButton_quantity.isChecked():
            selection = 'quantity'
            name = self.QuantityLineEdit.text().strip()
        
        elif self.radioButton_description.isChecked():
            selection = 'description'
            name = self.DescriptionLineEdit.text().strip()
        
        elif self.radioButton_location.isChecked():
            selection = 'location'
            name = self.LabelLineEdit.text().strip()
            name = self.DrawerLineEdit.text().strip()
            name = self.ElseLineEdit.text().strip()
        
        elif self.radioButton_all.isChecked():
            selection = 'all'
            #I dont know how to impliment this yet
            #name = self.name_line_edit.text().strip()
        
        else:
            selection = 'N/A'
        
        
        results_list = searcher(tokenVal, selection)
        
        for item in results_list:
            print()         #1 set to cp
        output_writing(results_list)      #the other to an output file    
        
        
        
        
