import os, shutil, sys

def organize(searchString):    
    
    searchPath='/home/biju/Study/Books/Mathematics/Math Library/Miscellany/'
    destPath='/home/biju/Study/Books/Mathematics/Math Library/'
    
    for folderName,subfolders, filenames in os.walk(searchPath):
        for filename in filenames:
            if filename.__contains__(searchString):
                print ('Moving: '+filename)
                if not (os.path.exists(destPath+searchString)):
                    os.makedirs(destPath+searchString)
                shutil.move(searchPath+filename, destPath+searchString)

if __name__ == '__main__':
    organize(sys.argv[1])