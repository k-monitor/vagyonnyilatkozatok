from os import listdir
import json

files = listdir('pdf')

with open('PDFadatlapok.json', 'wb') as outfile:
    json.dump(files, outfile)
