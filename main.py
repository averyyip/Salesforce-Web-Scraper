from scraper import scraping
from DataToFile import *
from IDIterator import id_counter_generator
import pandas as pd

# test1 = "08730000000BrbOAAS" #lightning with pm
# test2 = "0873A000000cNNaQAM" #under point with no pm
# test3 = "0873A000000cMZQQA2" #under point no comments

file_name = "Idea Exchange List Mastersheet.xlsx"

id_iterator = id_counter_generator(file_name)
results = pd.DataFrame(columns=["Status","PM_Response", "Date", "Solution", "Details", "Comment1", "Comment2", "Comment3", "Comment4", "Comment5", "Comment6", "Comment7", "Comment8", "Comment9", "Comment10"])

counter = 0
for idea_id in id_iterator:
	scraped_idea = scraping(idea_id)
	results = addToDataFrame(results, *scraped_idea)
	counter += 1
	print(counter)

existing_excel = pd.read_excel(file_name)
results = pd.concat([existing_excel, results], axis=1)

createExcel(results)
