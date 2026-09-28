import requests
import json

res = requests.get("https://api.github.com")

print(res)
print(res.text)
print(type(res.text))

parseData = res.json()
print((parseData[  "user_search_url"]))
# print(type(res.text))
# print(res.status_code)
# print(parseData)
# print(type(parseData))

# """this code is for showing the reposnse of the api and how the server 
# repsonds with json data which python sees as string
# then we converted into a dic using json() """



# print(parseData["user_search_url"])

# """
# | Attribute / method            | What it gives you                |
# | ----------------------------- | -------------------------------- |
# | `response.status_code`        | HTTP status code                 |
# | `response.ok`                 | Whether status indicates success |
# | `response.reason`             | Status description               |
# | `response.url`                | Final/requested URL              |
# | `response.text`               | Body as text                     |
# | `response.content`            | Body as bytes                    |
# | `response.json()`             | Parse JSON response              |
# | `response.headers`            | Response headers                 |
# | `response.cookies`            | Cookies                          |
# | `response.request`            | Original request object          |
# | `response.raise_for_status()` | Raises for HTTP error responses  |
# """

import requests
