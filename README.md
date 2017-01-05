# Salesforce-Web-Crawling
Project created for a Salesforce Externship by Shiv and Avery

This program takes a spreadsheet containing Idea IDs (that are presorted by number of upvotes), scrapes/extracts the corresponding data
fields of the ideas on www.salesforce.com/ideaSearch, and organizes all of this data in a new spreadsheet

IDIterator.py provides the functionality related to reading the excel spreasheet and outputting a generator that returns Idea Ids

scraper.py provides the functionality related to extracting the data from the website

DataToFile.py provides the functionality related to writing and organizing the data to a new excel spreasheet

main.py runs the entire program and executes the aforementioned files
