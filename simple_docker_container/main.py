import requests
"""
All of this code is arbitrary for the sake of this tutorial.
It is only used to demonstrate a script that requires
a third party package ('requests')
"""


# sending a get request
request = requests.get("https://www.google.com/")

# printing request info that is returned
print("Status Code: {}".format(request.status_code))
print("URL: {}".format(request.url))
print("Request: {}".format(request.request))