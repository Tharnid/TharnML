import requests
import json
BASE_URL = 'https://api.github.com'
Link_URL = 'https://git.github.com'
Username = 'Tharnid'
api_token = '1f8022c6235a97af319a750614080637a6823f0a'
header = {  'X-Github-Username': '%s' % username,
            'Content-Type': 'application/json',
            'Authorization': 'token %s' % api_token,
}
