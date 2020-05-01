import requests

CONSUMER_KEY = ""
CONSUMER_SECRET = "" 

def getBearerToken():
    response = requests.post(
      'https://api.twitter.com/oauth2/token', 
      auth=(CONSUMER_KEY, CONSUMER_SECRET),
      data={'grant_type': 'client_credentials'})

    if response.status_code is not 200:
      raise Exception("Cannot get a Bearer token (Status Code %d) Message: %s" % (response.status_code, response.text))

    body = response.json()
    return body['access_token']