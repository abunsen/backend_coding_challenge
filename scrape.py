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

#getting the urls for each of the result pages
#missed the second underscore in the class "result__url" and had a massive time sink here


#tried to find the most elegant solution for handling adding each individual hash result
#massive time sink here
for url in soup.select(".result__url"):
     result_hash = {}
     result_hash['url'] = url.get_text().strip()
     results_array.append(result_hash)

# gettting title of result page
for title in soup.find_all('h2'):
    results_array[i]['title'] = title.get_text().strip()
    i += 1


result['search_term'] = search_term
result['result_count'] = i
result['results'] = results_array
print result

#there were nothing akin to a description for each of the results on the page
#therefore they are omitted
#using both of these loops is not the most efficient considering they
# O(n) each
#total runtime is O(n) + O(n)
#severe potential for bottleneck with this solution
#the order of the keys in the result hashes are in the incorrect order. ran out of time
# to correct
#i am aware it would be a problem for feeding the returned JSON to a potential API
#would fix if given more time
