import os
import shutil

FOLDER_NAME = "SORTED-FILES" #chose to give any folder name

extensions = {
            ".txt":"Documents",
            ".pdf":"Documents",
            ".doc":"Documents",
            ".docx":"Documents",
            ".xls":"Documents",
            ".webp":"Documents",
            ".py":"Code",
            ".c":"Code",
            ".cpp":"Code",
            ".js":"Code",
            ".html":"Code",
            ".png":"Pictures",
            ".jpg":"Pictures",
            ".JPG":"Pictures",
            ".mp3":"Audio and Video",
            ".mp4":"Audio and Video",
            ".wav":"Audio and Video",
            ".gif":"Audio and Video",
            ".mkv":"Audio and Video",  
            ".zip":"Archived",
            ".rar":"Archived",
            ".exe":"Applications"
            }

def get_path(current):
    home = os.environ['USERPROFILE']  # this function finds the desktop and organizes it
    home = os.path.join(home,"Desktop",current)   # you can change current or add additonal argument here to sort other file
    home = home.replace("\\","/")
    return home

def make_main_dir(path):  #this function makes the main sorted folder,containing all subfolders
    os.chdir(path)
    name = FOLDER_NAME #change this to a different name if needed,will be the name of the folder containing all  files
    if not os.path.exists(name):
        os.mkdir(name)
    return name

def make_subdirs(path): # this function makes all the subfolders,containing files
    os.chdir(path) 
    for k in extensions.values():
        if not os.path.exists(k):
            os.mkdir(k)

def get_all_files(source):  # this function gets all the files and  sorts them according to subfolders
    os.chdir(source)
    for i in os.listdir():
        _,ext = os.path.splitext(i)
        
        for key,value in extensions.items():
            if key == ext:
                shutil.move(i,f"{FOLDER_NAME}/{value}")

def go_back(src,dst):  #function that erases the action and un-sorts all files
    os.chdir(src)
    print(os.getcwd())
    for dir in os.listdir():
        for file in os.listdir(dir):
            shutil.move(src + "/" + dir + "/" + file,dst)
        
        os.rmdir(src + "/" + dir)
       
where = input("Please choose where to sort and store,press only enter for desktop:")
src = get_path(where) # get the CHOSEN LOCATION as path
maindir = make_main_dir(src)  # make the main directory in CHOSEN LOCATION
make_subdirs(maindir)  # make the subfolders in the main dir
get_all_files(src) #sort all files in the chosen dir

erase = input("Would you like to cancel changes(Y or N):")

if erase == "Y" or erase == "y":
    go_back(src + f"/{FOLDER_NAME}",get_path(where))
    os.chdir(src)
    os.rmdir(src + f"{FOLDER_NAME}")




