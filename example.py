import json
from os import getenv
from tenablescwrapper.authenticate import authenticate
from tenablescwrapper.analysis import analysis

with open('./queries/vulndetail_query.json', 'r') as vuln_query_f:
    vulndetail_query = json.load(vuln_query_f)

sc_username = getenv('SC_USERNAME')
sc_password = getenv('SC_PASSWORD')

credentials = {'username': sc_username, 'password': sc_password}

security_center_hostname = 'tenable.nodomain.lan'

security_center_auth_data = authenticate(
    security_center_hostname, credentials)

vulndetail_results = analysis(
    security_center_auth_data['headers'],
    security_center_auth_data['cookies'],
    security_center_hostname,
    json.dumps(vulndetail_query)
)

print(json.dumps(vulndetail_results))
