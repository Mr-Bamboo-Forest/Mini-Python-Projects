import os 
import shutil 

path = input("Enter the path: ")
files = os.listdir(path)

for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else: 
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)

        #paste in dir in terminal when asked for it eg, Enter the path (e.g.): C:\Users\Downloads
