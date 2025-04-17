import os
def walking(path):
    for currentdir,foldernames,filenames in os.walk(path):
        print("Current Directory :",currentdir)
        print("")
        for folder_name in foldernames:
            print("Folder name :",folder_name)
        print("")
        for file_name in filenames:
            print("File name :",file_name)
        print("")
        print("-"*100)

path = input("Enter path : ") 
print("\n")
walking(path)