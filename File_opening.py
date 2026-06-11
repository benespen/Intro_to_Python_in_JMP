# File opening

# file opening standard method
def return_file_text(filename):
     try:
         file = open(filename)
     except:
         return "Error opening file!"
     file_text = file.read()
     return file_text