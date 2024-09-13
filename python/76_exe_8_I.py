import pypdf
import os

writer=pypdf.PdfWriter()

path="D:/programs/python/"
a=os.listdir("D:/programs/python/")
pdflist=[]
for i in a:
    if i.endswith('.pdf'):
        pdflist.append(i)

for i in pdflist:
    writer.append(i)

path+='merged-pdf by sahil.pdf'
writer.write('merged-pdf by sahil.pdf')
writer.close()






