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
    """
    Will take relevant outputs from comparisons and write to files as needed
    
    NOT IMPLIMENTED still figuring out how I want this displayed or in a file at all
    """
    pass

                
def searcher(tokenVal, choice):
    """
    Searches the input CSV file for a token
    """
    with open('IEEE Catalogue Fall 24 -Cole - Parts Shelf.csv', 'r') as input_file:
        #with open('search_results.csv', 'w', newline='') as ourput_csv_file:
                
            
        match choice:               #personal preference for switch statements
            case 'name':
                slelction = 1
            case 'quantity':
                slelction = 13
            case 'description':
                slelction = 8       #should be 7, but accedentally have extra comma in the file
            case 'location':
                slelction = 15
            case 'all':
                slelction = -1
            case _:
                slelction = 0

        #content = csv.writer(ourput_csv_file)
        #content.writerow(['Item_Name','','Quantity','','Location','','Desc_an_Other_Info'])
        
        list_o_lines = []       #list for all valid matches
        
        if slelction > 10:
            slelction -= 10
            for line in input_file:
                if line:
                    line = line.rstrip()
                    line_split = line.split(',')

                    if line_split[slelction]:
                        if re.search(tokenVal, line_split[slelction]):
                            list_o_lines.append(line)
                        
        else:
            for line in input_file:
                if line:                            #clean up input line and seperate by comma, if it exists
                    line = line.rstrip()
                    line_split = line.split(',')
                    
                    if line_split[slelction]:       #if the section being searched is not empty, see if it matches the token
                        if tokenVal in line_split[slelction]:
                            list_o_lines.append(line)
                        
        return list_o_lines
        
            
            
            
            
            
        """
                            print("In {0} search for \"{1}\"".format(line_split[slelction], tokenVal))


        hold = 0
        for x in order_preserver:
            output_txt_file.write(f'{x:40s} - {counter_dict.get(x)} \n')
            hold += counter_dict.get(x)

        output_txt_file.write('-------------------------------------------------\n')
        output_txt_file.write(f'{"Total emails":40s} - {hold}')
        """