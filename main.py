from scraper import scraping
from DataToFile import *
from IDIterator import id_counter_generator
import pandas as pd

#Edit file_name to choose which sheet to use for idea id inputs
file_name = "test.xlsx"

#Creates Excel File of Scraped Data
def save_progress(scraped_data_frame):
	input_data_frame = pd.read_excel(file_name)
	resulting_data_frame = pd.concat([input_data_frame, scraped_data_frame], axis=1)
	createExcel(resulting_data_frame)
	print("Progress Saved")

id_iterator = id_counter_generator(file_name)
results = pd.DataFrame(columns=["Status","PM_Response", "Date", "Solution", "Details", "Comment1", "Comment2", "Comment3", "Comment4", "Comment5", "Comment6", "Comment7", "Comment8", "Comment9", "Comment10"])
counter = 0

#Scrapes each idea and Saves to Data Frame
for idea_id in id_iterator:
	print("------------------------------")
	scraped_idea = scraping(idea_id)
	results = addToDataFrame(results, *scraped_idea)
	counter += 1
	print(counter)
	if counter % 100 == 0: #Saves progress every 100 entries
		save_progress(results)

#Saves final progress
save_progress(results)
