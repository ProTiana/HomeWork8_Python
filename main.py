from os.path import exists
from csv_create import creating
from writing_data import writing_scv
from writing_data import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
   creating()

writing_scv()
writing_txt()