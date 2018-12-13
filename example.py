import json
from os import getenv
from urllib3 import disable_warnings, exceptions
from tenablescwrapper.authenticate import authenticate
from tenablescwrapper.analysis import analysis

disable_warnings(exceptions.InsecureRequestWarning)

# Get authentication and hostname information for Tenable from config.json file
with open('./config.json', 'r') as config_f:
    config = json.load(config_f)

credentials = {'username': config['username'], 'password': config['password']}

security_center_hostname = config['sc_host']

# Read the Vulnerability Detail query from file (which will be submitted to /analysis API endpoint)
with open('./queries/vulndetail_query.json', 'r') as vuln_query_f:
    vulndetail_query = json.load(vuln_query_f)

# Authenticate to Tenable Security Center API
security_center_auth_data = authenticate(
    security_center_hostname, credentials)

# Query the Tenable Security Center /analysis API endpoint for Vulnerability Details
vulndetail_results = analysis(
    security_center_auth_data['headers'],
    security_center_auth_data['cookies'],
    security_center_hostname,
    json.dumps(vulndetail_query)
)

# Print results
print(json.dumps(vulndetail_results))
