'''
Project DESC: Read from PDF 

'''

#below lib needs Ghostscript + tk libraries to get camelot-py installed correctly
import camelot
from pathlib import Path

my_path = Path(__file__).resolve().parent

file_path = my_path / "sample_tables.pdf"

#read all tables from pdf file
tables = camelot.read_pdf(file_path, pages = "1")

#generate zip folder containing all csv files extracted from the pdf-text type
tables.export("output.csv", f='csv', compress=True)

#Generate output.csv file in working directory
tables[1].to_csv('output.csv')
print(tables)

