# import requests
# from jsonpath import jsonpath

# token = 'bdb2c4d3cb5dbf43c19bde857afb74246017aee8'
# headers = {'Authorization': 'Token {token}'.format(token=token)}
# baseurl = 'http://localhost:8000/api/v1/companies'

# url = '{baseurl}/{id}/'.format(baseurl=baseurl, id=2)
# res = requests.get(url=url, headers=headers)
# employees = jsonpath(res.json(), 'employees')

# print(type(employees))

import requests
from jsonpath import jsonpath

token = 'bdb2c4d3cb5dbf43c19bde857afb74246017aee8'
headers = {'Authorization': 'Token {token}'.format(token=token)}
baseurl = 'http://localhost:8000/api/v1/employees'

url = '{baseurl}/{id}/'.format(baseurl=baseurl, id=3)
res = requests.get(url=url, headers=headers)
print(res.json())
company = jsonpath(res.json(), '$[0].company')

print(len(company))
