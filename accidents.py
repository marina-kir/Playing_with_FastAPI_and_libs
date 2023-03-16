import requests


import urllib
url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=595955cf-914f-42e1-bd97-cf6211c6e4e5&limit=5&q=title:jones'
fileobj = requests.get(url)



print (fileobj.text)
print (":)")