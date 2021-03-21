import PyPDF2
import re
import os
import subprocess
import sys
import tkinter as tk
import PDFGui
from PDFGui import Application

root = tk.Tk()
app = Application(master=root)
app.mainloop()

if app.all_input_selected == True:

    #Opens and reads the PDF File
    for filename in os.listdir("."):
        if filename.endswith('.pdf'):
            file = filename

    pdffile = open(file, 'rb')
    readpdf = PyPDF2.PdfFileReader(pdffile)
    print(file)

    #Gets the number of pages in the PDF
    numpages = readpdf.getNumPages()

    #Define keyterms
    Street = app.save_Street.lower()
    
    Street = Street.replace("avenue", "ave")
    Street = Street.replace("street", "st")
    Street = Street.replace("court", "ct")
    Street = Street.replace("road", "rd")
    Street = Street.replace("boulevard", "blvd")
    Street = Street.replace("lane", "ln")
    Street = Street.replace("drive", "dr")
    Street = Street.replace("place", "pl")
    Street = Street.replace("circle", "cir")

    def WordFixer(string):
        string = string.replace('ave', 'av')

    HouseNumber = app.save_Number
    print(HouseNumber)

    def is_valid_data(string):
        ret_val = True
        if string.count('.') >= 2: 
            ret_val = False
        elif string == ' ' or string == '':
            ret_val = False
        
        return ret_val

        
    # creating a page object  
    firstPage = readpdf.getPage(0)  
    secondPage = readpdf.getPage(1)
    
    # extracting text from page  
    text = firstPage.extractText() 
    text2 = secondPage.extractText()

    #take off the "Index" at the front of the string
    text = text + text2
    split = text.splitlines()

    #create an empty list to put the addresses in 
    clean_split = []

    for val in split:
        if is_valid_data(val):
            clean_split.append(val.lower())
        
        
    combined_string = ' '.join(clean_split)
    print(combined_string)
    #find the index in the string where the road is 
    loc = combined_string.find(Street)

    #as long as it is in the string of names, we will get all of the numbers right after it
    if loc != -1:
        #move past the street name itself
        #while not combined_string[loc].isnumeric() :
        #    loc += 1
        loc += len(Street)

        pagesearchnumbers = ""
    
        while not combined_string[loc].isalpha():
            pagesearchnumbers += combined_string[loc]
            loc += 1
    
            if loc >= len(combined_string):
                break

        pagesearchnumbers = pagesearchnumbers.strip()
    
        split_numbers = pagesearchnumbers.split(', ')
        for i, val in enumerate(split_numbers):
            print(val)
            split_numbers[i] = val.split(' ')[0]
            print(split_numbers[i])

        #cast all of the page numbers as ints
        numbers = [int(val) + 2 for val in split_numbers]
        print(numbers)

        for t in (numbers): #Searches the pages gotten from previous for loop for the address
            PageObjAddress = readpdf.getPage(t)
            AddressText = PageObjAddress.extractText()
            print(AddressText)
            WordFixer(AddressText)
            AddressSearch = re.search(HouseNumber, AddressText, re.IGNORECASE)
            if(AddressSearch != None):
                pagenum = (t) #Adding one because python counts from 0
                page = 'page=' + str(pagenum)

                path_to_pdf = os.path.abspath(file)

                path_to_acrobat = os.path.abspath('C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe') 

                process = subprocess.Popen([path_to_acrobat, '/A', page, path_to_pdf], shell=False, stdout=subprocess.PIPE)
                process.wait()
                sys.exit(0)

  
print("Address not found")
