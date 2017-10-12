import sys
import requests
import json
import bs4

search_term = sys.argv[1]
response = requests.get('https://duckduckgo.com/html/?q=' + search_term)
soup = bs4.BeautifulSoup(response.text, "html.parser")
# print soup
result = {}
results_array = []
# counter for number of results
i = 0

# #getting the urls for each of the result pages
for url in soup.select(".result__url"):
    print url.get_text()
    #
    #
    # gettting title of result page
for title in soup.find_all('h2'):
    print(title.get_text())
    i += 1
# #
# # #printing number of results
# print 'Nuber of results: ' + str(i)
result['search_term'] = search_term
result['result_count'] = i
print result
