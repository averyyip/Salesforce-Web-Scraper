from bs4 import BeautifulSoup
import urllib.request


#Retrieves text from html & Removes all whitespace and tags
def html_text_getter(html):
	return html.get_text().strip(" \t\n\r")

#Retrieves Status of Idea
def get_status(soup):
	status = soup.find("span", {"class":"comty-status-badge"})
	return html_text_getter(status)

#Retrieves PM Response(Y/N) and Date of Last PM Response, Provided HTML Solution, body of Response
def get_pm_response(soup):
	latest_comment_section = soup.find("div", {"id":"ideaView:ForumLayout:ideaViewForm:latestCommentSection"})
	if latest_comment_section:
		date = html_text_getter(latest_comment_section.find("span", {"class":"cmp-text-body--small"}))
		detail = html_text_getter(latest_comment_section.find("div", {"class":"htmlDetailElementDiv"}))
		solution = latest_comment_section.find("a", {"target": "_blank"}) #did not want to accidentally ruin html link
		
		if solution:
			return "Y", date, solution.get_text(), detail
		else:
			return "Y", date, "N/A", detail
	else:
		return "N", "N/A", "N/A", "N/A"

#Retrieves all comments from an idea
def get_comments(soup):
	iter_comments = soup.find_all("li", class_="cmp-comments-list")
	return list(get_comments_text(iter_comments))

def get_comments_text(iterable_soup):
	for elem in iterable_soup:
		yield html_text_getter(elem.find("div", {"class":"htmlDetailElementDiv"}))

def scraping(id):
	html = urllib.request.urlopen("https://success.salesforce.com/ideaView?id=" + id)
	soup = BeautifulSoup(html, "html.parser")

	#Status (ex. Deliver in Lightning, Under consideration, etc.)
	status = get_status(soup)
	
	#PM Response Information
	pm_response, date, solution, details = get_pm_response(soup)

	#Comments
	comment_array = get_comments(soup)

	#Testing
	# print("Status: " + status)
	# print("PM Response: " + pm_response)
	# print("Last Response Date: " + date)
	# print("HTML Solution: " + solution)
	# print("PM Response Details: " + details)
	# for i in range(len(comment_array)):
	# 	print("----------------------------------------")
	# 	print(comment_array[i])
	return [status, pm_response, date, solution, details] + comment_array[0:10] #top 15 comments

# scraping(test1)
# scraping(test2)
# scraping(test3)
