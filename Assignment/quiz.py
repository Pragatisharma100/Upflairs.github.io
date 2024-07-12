import shutil
import os
for i in os.listdir(r"C:\Users\Pragati\Desktop\Upflairs\Assignment\Data"):
    if i.endswith(".txt"):
        shutil.move(r"C:\Users\Pragati\Desktop\Upflairs\Assignment\Data"+'\\'+i,r"C:\Users\Pragati\Desktop\Upflairs\Assignment\TEXT FOLDER"+'\\'+i)
    elif i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png"):
        shutil.move(r"C:\Users\Pragati\Desktop\Upflairs\Assignment\Data"+"\\"+i,r"C:\Users\Pragati\Desktop\Upflairs\Assignment\IMAGE FOLDER"+"\\"+i)
    elif i.endswith(".pdf"):
        shutil.move(r"C:\Users\Pragati\Desktop\Upflairs\Assignment\Data"+"\\"+i,r"C:\Users\Pragati\Desktop\Upflairs\Assignment\PDF FOLDER"+"\\"+i)
# if a.split(".")[1] =="txt":
#     print("text file")