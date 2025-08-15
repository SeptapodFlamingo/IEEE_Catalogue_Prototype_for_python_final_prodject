"""

File to take UI elements and give them function



"""

from PyQt6.QtWidgets import *
from IEEECatSearchGUI import *
import csv
from catallogue_searcher import *



class Search(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        bb
        """
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(lambda : self.search_event())
        self.pushButton_clear.clicked.connect(lambda : self.clear_values())
        
        self.radioButton_all.toggled.connect(lambda : self.unfinished_message())
             
        
    def unfinished_message(self):
        """
        bb
        """
        self.clear_radio()
        self.error_indicator.setText('Unfinished section, please re-select')
        #if self.radioButton_name.isChecked():
        self.radioButton_all.setChecked(False)

        
    def clear_values(self):
        """
        bb
        """
        self.clear_radio()
        self.clear_text()
        
    def clear_text(self):
        """
        bb
        """
        self.NameLineEdit.clear()
        self.QuantityLineEdit.clear()
        self.DescriptionLineEdit.clear()
        self.LabelLineEdit.clear()
        self.DrawerLineEdit.clear()
        self.ElseLineEdit.clear()
        
    def clear_radio(self):
        """
        bb
        """
        
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
        """
        bb
        """
        
        #take info from text boxes as relevant, checking radiobuttons
        if self.radioButton_name.isChecked():
            selection = 'name'
            nameline = self.NameLineEdit.text().strip()
            tokenVal = nameline
        
        elif self.radioButton_quantity.isChecked():
            selection = 'quantity'
            quantityline = self.QuantityLineEdit.text().strip()
            tokenVal = quantityline
        
        elif self.radioButton_description.isChecked():
            selection = 'description'
            descriptionline = self.DescriptionLineEdit.text().strip()
            tokenVal = descriptionline
        
        elif self.radioButton_location.isChecked():
            selection = 'location'
            labelline = self.LabelLineEdit.text().strip()
            drawerline = self.DrawerLineEdit.text().strip()
            elseline = self.ElseLineEdit.text().strip()
            
            tokenVal = labelline + drawerline
        
        elif self.radioButton_all.isChecked():
            selection = 'all'
            #I dont know how to impliment this yet
            #name = self.name_line_edit.text().strip()
        
        else:
            selection = 'N/A'
        
        
        
        results_list = searcher(tokenVal, selection)
        
        
        print("\n\nRelevant results:")
        for item in results_list:
            print("\t")
            print(item)                     #Send to command line
        print("End of search results\n\n")
        output_writing(results_list)        #the other to an output file    
        
        
        
        
        """
        #dealing with inconvertable values
        invalid_quantity= True
        
        if quantity_str.isdigit():
            quantity = int(quantity_str)
            if quantity >= 0:
                invalid_quantity= False
        if invalid_quantity:
            self.error_indicator.setText('Enter a valid quantity')
        else:
            self.clear_radio()
                
            with open('search_results.csv', 'w', newline='') as output_csv_file:
                content = csv.writer(output_csv_file)
                #content.writerow(['Name', 'Age', 'Selection'])     #this line should already exist
                content.writerow([Item_Name, '', Quantity, '', Location, '', Desc_an_Other_Info])
                
        """