from PyPDF3 import PdfFileReader
import re

file = PdfFileReader(open("winthrop.pdf", "rb"))

# print how many pages input1 has:
print("winthrop.pdf has %d pages." % file.getNumPages())


def is_valid_data(string):
    ret_val = True
    if string.count('.') >= 2: 
        ret_val = False
    elif string == ' ' or string == '':
        ret_val = False
        
    return ret_val

        
# creating a page object  
firstPage = file.getPage(0)  
secondPage = file.getPage(1)
    
# extracting text from page  
text = firstPage.extractText() 
text2 = secondPage.extractText()

#take off the "Index" at the front of the string
text = text + text2
split = text.splitlines()

clean_split = []

for val in split:
    if is_valid_data(val):
        clean_split.append(val)
        
        
combined_string = ' '.join(clean_split)

#find the index in the string where the road is 
loc = combined_string.find("Butterfield Rd")

#as long as it is in the string of names, we will get all of the numbers right after it
if loc != -1:
    #move past the street name itself
    while not combined_string[loc].isnumeric() :
        loc += 1
        
    numbers = ""
    
    while combined_string[loc].isnumeric() or combined_string[loc] == ',' or combined_string[loc] == ' ':
        numbers += combined_string[loc]
        loc += 1
    
        if loc >= len(combined_string):
            break
    
    #cast all of the page numbers as ints
    numbers = [int(val) for val in numbers.split(',')]
    
    print(numbers)
    
    #look in the pdf for which street number it is on 
    for i in numbers:
         PageObj = file.getPage(i - 1)
         Text = PageObj.extractText()
         #print(Text)
         if re.search("1n231", Text, re.IGNORECASE):
              print("Pattern Found on Page: " + str(i))
         else:
             print("Pattern not found on", i)
    
else:
    print("Not in the pdf")
    
#print(combined_string)
    
        

#print(text)
"""def save_page_num(my_dict, street_name, page_nums):
     #split it by the comma
     nums_split = page_nums.split(',')
     
     #check if there is an endline in the page nums 
     #nums_split = [val.replace('\n', '') for val in nums_split]
     #if '\n' in nums_split: 
     #    separate_newline = nums_split.split('\n')
     #    next_num = separate_newline[1]
     #    nums_split = separate_newline[0]
         
     #print(nums_split)
     #print(next_num)             
         
     #cast to int and save in dictionary
     my_dict[street_name] = nums_split
     

my_dict = {}

#we are starting looking at the name
looking_at_name = True
looking_at_number = False 
this_name = ""
these_numbers = ""

#turn the string into a dictionary 
for char in text:
    if looking_at_name:
        #if it is not an empty string 
        if char == '.':
            looking_at_name = False
            looking_at_number = True 
        elif char != '\n':
            this_name += char
        
    else: #if looking at numbers 
        # keep track of all of the numbers
        if char == '.':
            continue
        
        #once we have reached the end of the periods, we know that we are now looking at the number
        else:
            looking_at_number = True 
        
        if looking_at_number:
            #once we reach an alphabet character, we want to switch back to reading a letter 
            if char.isalpha():
                #strip off any extra whitespace 
                these_numbers = these_numbers.strip()
                this_name = this_name.strip()
                save_page_num(my_dict, this_name, these_numbers)

               
                #reset the variables to look at the next address
                looking_at_name = True
                these_numbers = ""
                this_name = char
            
           #elif char == '\n':
           #     print(these_numbers)
                
             #If we are still looking at numbers  
            else: 
                these_numbers += char
                                
#print(my_dict)
        
        

#take out all of the periods
split = text.replace('.', '')

#for i in range  
split = split.split('\n')

#remove empty elements from the list
while("" in split) : 
    split.remove("") 
    
while(" " in split) : 
    split.remove(" ") 


#print(split)"""