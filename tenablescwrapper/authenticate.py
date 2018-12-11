import json
import requests


def authenticate(sc_hostname: str, creds: dict = None) -> dict:
    '''Authenticate to the Security Center API and return
    the authentication headers and cookies for subsequent requests'''

    if not sc_hostname or not creds:
        raise TypeError('Missing arguments - sc_hostname or creds')

    token_response = requests.post('https://' + sc_hostname + '/rest/token',
                                   data=json.dumps(creds), verify=False)

    token_data = token_response.json()

    cookies = token_response.cookies

    token = str(token_data['response']['token'])

    headers = {'X-SecurityCenter': token,
               'Content-Type': 'application/json',
               'METHOD': 'POST'}

    return {'headers': headers, 'cookies': cookies}
