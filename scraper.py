from bs4 import BeautifulSoup
import pandas as pd
import urllib.request

test1 = "08730000000BrbOAAS" #lightning with pm
test2 = "0873A000000cNNaQAM" #under point with no pm
test3 = "0873A000000cMZQQA2" #under point no comments

#Retrieves text from html & Removes all whitespace and tags
def html_text_getter(html):
	return html.get_text().strip(" \t\n\r")

#Retrieves Status of Idea
def get_status(soup):
	status = soup.find("span", {"class":"comty-status-badge"})
	return html_text_getter(status)

#Retrieves PM Response(Y/N) and Date of Last PM Response
def get_pm_response(soup):
	latest_comment_section = soup.find("div", {"id":"ideaView:ForumLayout:ideaViewForm:latestCommentSection"})
	if latest_comment_section:
		date = html_text_getter(latest_comment_section.find("span", {"class":"cmp-text-body--small"}))
		solution = latest_comment_section.find("a", {"target": "_blank"}).get_text()
		return "Y", date, solution
	else:
		return "N", "N/A", "N/A"

#Retrieves all comments from an idea
def get_comments(soup):

#Retrieves description of idea
def get_description(soup):

def scraping(id):
	html = urllib.request.urlopen("https://success.salesforce.com/ideaView?id=" + id)
	soup = BeautifulSoup(html, "html.parser")

	#Status (ex. Deliver in Lightning, Under consideration, etc.)
	status = get_status(soup)
	
	#PM Comment Information
	pm_response, date, solution = get_pm_response(soup)

	#Testing
	print(status, pm_response, date, solution)
	return pm_response

scraping(test1)
scraping(test2)
scraping(test3)
