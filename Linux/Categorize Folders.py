import os, shutil
path='/home/biju/Study/Books/Mathematics/Recreational Math Collection/'
searchString = 'Discrete'
for folderName,subfolders, filenames in os.walk(path):
 	for filename in filenames:
         if filename.__contains__(searchString):
             print (filename)
             shutil.move(path+filename, path+'Discrete')
