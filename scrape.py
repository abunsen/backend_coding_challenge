import sys
import requests
import json

search_term = sys.argv[1]
response = requests.get('http://api.duckduckgo.com/?q='+search_term+'&format=json')
result_count = 0
results = []
topics = response.json()['RelatedTopics']
i = 0
while i <= 2:
    results.append({ "desc": topics[i]['Text'], "url": topics[i]['FirstURL']})
    i += 1
    result_count += 1

print i

# while i < len(topics):
#     print topics[i]['Topics'][0]
#     i += 1
# len(topics[i]['Topics'])
while i < len(topics):
    j = 0
    while j < len(topics[i]['Topics']):
        results.append({ "desc": topics[i]['Topics'][j]['Text'], "url": topics[i]['Topics'][j]['FirstURL']})
        j += 1
        result_count += 1
    i += 1

return_json = {}
return_json['search_term'] = search_term
return_json['result_count'] = result_count
return_json['results'] = results

print return_json
