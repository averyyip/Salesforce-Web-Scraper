import pandas as pd 

#TO USE: READ NOTE IN LINE 10


#Generator Object that returns IDs
def id_counter_generator(file_name):
    b = True
    index = 0
    datafield = pd.read_excel(file_name) #Replace Workbook2.csv with filename
    while b:
        try:
            index += 1
            yield datafield['Idea ID'][index - 1]
        except:
            b = False


#Example Generator code
# x = IDCounterGenerator()
# for d in x:
# 	print(d)
