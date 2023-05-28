"""
This program walks through a folder tree
and searches for files with a certain file extension
(like .pdf or .jpg)
It should copy these files from whatever location they are in
to a new folder
"""
import shutil, os
from pathlib import Path

# Specify here the wanted file type you want to search for
wantedFileType = ".jpg"
# Use os.walk to walk through a folder tree in a for loop
for folderName, subfolders, fileNames in os.walk("C:\\Users\\nermi\\PycharmProjects\\pythonProject"):
    # Make a nested for loop that searches for files in folders
    for fileName in fileNames:
        # For each file in sub folder take the end of the file and compare it if its the file type we want
        if wantedFileType.lower() in fileName:
            # If the file type is the one we want then use shutil copy to copy the file to a new folder
            # Get the filepath of the file that got found by the loop
            filepath = os.path.join(os.path.abspath(folderName), fileName)
            # There is a bug with shutil.copy, so we go over the SameFileEror with a try/except block
            try:
                # copy the file with the filepath to the right directory
                shutil.copy(filepath, Path.cwd() / "pics")

            except shutil.SameFileError:
                pass
