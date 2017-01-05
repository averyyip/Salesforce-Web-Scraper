import pandas as pd


#TO USE: use addToDataFrame function to add all of the data into the dataframe.
#Then, use createExcel() to create the final excel file

# Adds given data to the dataFrame df, Returns a concatenated dataFrame
def addToDataFrame(frame, status, pm_response, date, solution, details, comment1, comment2, comment3, comment4, comment5, comment6, comment7, comment8, comment9, comment10):
	df2 = pd.DataFrame([[status, pm_response, date, solution, details, comment1, comment2, comment3, comment4, comment5, comment6, comment7, comment8, comment9, comment10]], columns=["Status","PM_Response", "Date", "Solution", "Details", "Comment1", "Comment2", "Comment3", "Comment4", "Comment5", "Comment6", "Comment7", "Comment8", "Comment9", "Comment10"])
	frames = [frame, df2]
	return pd.concat(frames, ignore_index=True)
	#print(df)


#Creates an excel spreadsheet based on dataframe df
def createExcel(frame):
	writer = pd.ExcelWriter('data.xlsx', engine='xlsxwriter')
	frame.to_excel(writer, sheet_name='Sheet1')
	writer.save()

#TESTING: Creates an example dataframe and creates an excel spreadsheet
# df = pd.DataFrame(columns=["Status","PM_Response", "Date", "Solution", "Details", "Comment1", "Comment2", "Comment3", "Comment4", "Comment5", "Comment6", "Comment7", "Comment8", "Comment9", "Comment10"])
# df = addToDataFrame(df, 3,2,2,2,2,2,2,2, 4, 4, 4, 4, 4, 4, 4)
# df = addToDataFrame(df, 3,2,2,2,2,2,2,2,4, 4, 4, 4, 4, 4, 4)
# df = addToDataFrame(df, 3,2,2,2,2,2,2,2,4, 4, 4, 4, 4, 4, 4)
# createExcel(df)
