import pandas as pd


#TO USE: use addToDataFrame function to add all of the data into the dataframe.
#Then, use createExcel() to create the final excel file


df = pd.DataFrame(columns=["Status","PM_Response", "Date", "Solution", "Details", "Comment1", "Comment2", "Comment3", "Comment4", "Comment5", "Comment6", "Comment7", "Comment8", "Comment9", "Comment10"])

# Adds given data to the dataFrame df
def addToDataFrame(status, pm_response, date, solution, details, comment1, comment2, comment3, comment4, comment5, comment6, comment7, comment8, comment9, comment10):
	df2 = pd.DataFrame([[status, pm_response, date, solution, details, comment1, comment2, comment3, comment4, comment5, comment6, comment7, comment8, comment9, comment10]], columns=["Status","PM_Response", "Date", "Solution", "Details", "Comment1", "Comment2", "Comment3", "Comment4", "Comment5", "Comment6", "Comment7", "Comment8", "Comment9", "Comment10"])
	global df
	frames = [df, df2]
	df = pd.concat(frames, ignore_index=True)
	#print(df)


#Creates an excel spreadsheet based on dataframe df
def createExcel():
	writer = pd.ExcelWriter('data.xlsx', engine='xlsxwriter')
	df.to_excel(writer, sheet_name='Sheet1')
	writer.save()

#Creates an example dataframe and creates an excel spreadsheet
addToDataFrame(3,2,2,2,2,2,2,2, 4, 4, 4, 4, 4, 4, 4)
addToDataFrame(3,2,2,2,2,2,2,2,4, 4, 4, 4, 4, 4, 4)
addToDataFrame(3,2,2,2,2,2,2,2,4, 4, 4, 4, 4, 4, 4)
createExcel()
