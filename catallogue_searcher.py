"""
catallogue_searcher.py

intended to be a seperate list of functions to search the CSV file for relevant results

	should sort listings alphabeticvally within each location when first called,
	then each location will be looked through with a version of binary search
	
todo: 
    add a way to search through listings that include a term, rather than exact matches
    add seperate dialogue window to display results rather than terminal and output file
    input and output formatting changes
"""
import csv
import re


#Item_Name,,Quantity,,Location,,Description_and_Other_Information

def output_writing(line_list):


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
                content.writerow([Item_Name,,Quantity,,Location,,Desc_an_Other_Info])
                
                
                
def searcher(tokenVal, choice):
    """
    Searches the input CSV file for a token
    """
    with open('IEEE Catalogue Fall 24 -Cole - Parts Shelf.csv.csv', 'r') as input_file:
        #with open('search_results.csv', 'w', newline='') as ourput_csv_file:
                
            
        match choice:               #personal preference for switch statements
        case 'name':
            slelction = 1
        case 'quantity':
            slelction = 3
        case 'description':
            slelction = 5
        case 'location':
            slelction = 7
        case 'all':
            slelction = -1
        default:
            slelction = 0
        



        #content = csv.writer(ourput_csv_file)
        #content.writerow(['Item_Name','','Quantity','','Location','','Desc_an_Other_Info'])
        
        list_o_lines = ['', '']
        
        for line in input_file:
            line = line.rstrip()
            line_split = line.split()
            if re.search(tokenVal, line_split[choice]):
                list_o_lines.append(line)
                
                
                
        return list_o_lines
        
            
            
            
            
            
            """
            hold = 0
            for x in order_preserver:
                output_txt_file.write(f'{x:40s} - {counter_dict.get(x)} \n')
                hold += counter_dict.get(x)

            output_txt_file.write('-------------------------------------------------\n')
            output_txt_file.write(f'{"Total emails":40s} - {hold}')
            """