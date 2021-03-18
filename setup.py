from cx_Freeze import setup, Executable
# NOTE: you can include any other necessary external imports here aswell
 
includefiles = ["PDFGui.py", "StormwaterandUtilityLocationIndexBookStreetIndexMobil.pdf"] # include any files here that you wish
excludes = []
packages = []
 
exe = Executable(
 # what to build
   script = "PDFReader.py", # the name of your main python script goes here 
   init_script = None,
   base = None, # if creating a GUI instead of a console app, type "Win32GUI"
   target_name = "PDF Reader", # this is the name of the executable file
   icon = None # if you want to use an icon file, specify the file name here
)
 
setup(
 # the actual setup & the definition of other misc. info
    name = "PDFReader", # program name
    version = "0.1",
    description = 'A general enhancement utility',
    author = "Dustin Osweiler",
    author_email = "dosweiler@carthage.edu",
    options = {"build_exe": {"excludes":excludes,"packages":packages,
      "include_files":includefiles}},
    executables = [exe]
)