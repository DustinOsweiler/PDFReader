import PyPDF2
import subprocess
import os
import fitz
import re
import tkinter as tk
import PDFGui
from PDFGui import Application

#root = tk.Tk()
#app = Application(master=root)
#app.mainloop()

#program = PDFReaderGui()
#program.window.mainloop()

#if program.all_input_selected == True:

    #Opens and reads the PDF File
    pdffile = open('StormwaterandUtilityLocationIndexBookStreetIndexMobil.pdf', 'rb')
    readpdf = PyPDF2.PdfFileReader(pdffile)

    #Gets the number of pages in the PDF
    numpages = readpdf.getNumPages()
    #print(numpages)

    #Define keyterms
    Address = save_address
    print(Address)

    #Parces the address
    def convert(lst): 
        return (lst[0].split())
    lst = Address

    Wheaton = [5,6,7,8,9,10,11,12,13,15,16,21,22,23,24,25,50,51,52,53,54,55,56,57,58,59,61]
    Winfield = [1,2,14]
    Naperville = [60]
    Glen_Ellyn = [28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,46,47,62,63,64,65,66,67,68,69,70,71,72,73]
    Lombard = [43,44,45,48,49,72,74,75,76,77]
    Carol_Stream = [3,4,17,18,19,20,26,27]

    print()

    for i in range(0, 1): #Searches the index for the street name
        PageObjStreet = readpdf.getPage(i)
        StreetText = PageObjStreet.extractText()
        print(streetText)
        StreetSearch = re.search(lst[1], StreetText, re.IGNORECASE)
        if(StreetSearch != None): #If we find the addresss we get the page number and put it in a string
            print("Street found in Index!")
            for t in range(3, numpages): #Searches the pages gotten from previous for loop for the address
                PageObjAddress = readpdf.getPage(t)
                AddressText = PageObjAddress.extractText()
                AddressSearch = re.search(Address, AddressText, re.IGNORECASE)
                if(AddressSearch != None):
                    pagenum = (t) #Adding one because python counts from 0
                    print(pagenum)
                    page = 'page=' + str(pagenum)

                    path_to_pdf = os.path.abspath('.\StormwaterandUtilityLocationIndexBookStreetIndexMobil.pdf')

                    path_to_acrobat = os.path.abspath('C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe') 

                    process = subprocess.Popen([path_to_acrobat, '/A', page, path_to_pdf], shell=False, stdout=subprocess.PIPE)
                    process.wait()
                    quit()

  
    print("Address not found")

#Check for Common Typos, Capitalization, Abbreviations