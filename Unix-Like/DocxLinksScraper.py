from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT

docx_file=input("Input docx filename (without .docx): ")
document = Document(docx_file + ".docx")
rels = document.part.rels
links=[]
f = open("links.txt", "w")

for rel in rels:
   if rels[rel].reltype == RT.HYPERLINK:
      links.append(rels[rel]._target)
      f.write(rels[rel]._target+"\n")
      print(rels[rel]._target)
f.close()
print("\n Links saved.")
