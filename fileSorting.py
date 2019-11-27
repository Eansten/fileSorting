import os
import shutil

path = "/#your folder path here#/" 
names = os.listdir(path)
folder_name = ['Photo', 'PDF', 'PHP', 'ISO', 'ZIP', 'EXE', 'Database', 'XML']
for x in range(0,8):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])

for files in names:
    if ".jpg" in files and not os.path.exists(path+'Photo/'+files):
        shutil.move(path+files, path+'Photo/'+files)
    if ".png" in files and not os.path.exists(path+'Photo/'+files):
        shutil.move(path+files, path+'Photo/'+files)
    if ".pdf" in files and not os.path.exists(path+'PDF/'+files):
        shutil.move(path+files, path+'PDF/'+files)
    if ".php" in files and not os.path.exists(path+'PHP/'+files):
        shutil.move(path+files, path+'PHP/'+files)
    if ".iso" in files and not os.path.exists(path+'ISO/'+files):
        shutil.move(path+files, path+'ISO/'+files)
    if ".zip" in files and not os.path.exists(path+'ZIP/'+files):
        shutil.move(path+files, path+'ZIP/'+files)    
    if ".exe" in files and not os.path.exists(path+'EXE/'+files):
        shutil.move(path+files, path+'EXE/'+files)
    if ".kdbx" in files and not os.path.exists(path+'Database/'+files):
        shutil.move(path+files, path+'Database/'+files)
    if ".xml" in files and not os.path.exists(path+'XML/'+files):
        shutil.move(path+files, path+'XML/'+files)