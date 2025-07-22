import os
from PyPDF2 import PdfMerger

def extracted(filename):
    name, _ = os.path.splitext(filename)

    try:
        return int(name) # if file name start with 1.pdf, 2.pdf
    except:
        return float('inf') # start with non-numeric interger
    

folder_path = r"D:\my apllication document\clg doc  xrox pdf"

files_list = [filename for filename in os.listdir(folder_path) if filename.lower() and filename.endswith(".pdf")]

files_list.sort(key = extracted)


merger = PdfMerger()

for filename in files_list:
    file_path= os.path.join(folder_path, filename)
    if os.path.getsize(file_path)>0:
        merger.append(file_path)
    else:
        print("file has 0 byte")

merger.write("file_marged.pdf")
merger.close()
print("marged complete")
