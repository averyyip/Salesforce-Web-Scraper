import pandas as pd 

#TO USE: READ NOTE IN LINE 9


#Iterator Object that returns IDs
class IDCounter:
    def __init__(self):
        self.datafield = pd.read_csv('Workbook2.csv') #REPLACE Workbook2.csv with the csv file in question
        self.index = 0

    def __iter__(self):
       return self
    def __next__(self):
        try:
            self.index += 1
            return self.datafield['Idea ID'][self.index - 1]
        except:
            raise StopIteration
#Example Iterator code
x = IDCounter()
for d in x:
	print(d)
