import requests


def analysis(headers: dict, cookies: str, sc_hostname: str,
             query: str) -> dict:
    '''Function used to query the /analysis API endpoint for Security Center'''
    if not headers or not cookies or not sc_hostname or not query:
        raise TypeError(
            'Missing parameter(s): headers, cookies, sc_hostname, or query provided to analysis')

    analysis_response = requests.post(
        'https://' + sc_hostname + '/rest/analysis', cookies=cookies,
        headers=headers, data=query, verify=False)

    analysis_response_json = analysis_response.json()
    if 'response' not in analysis_response_json.keys():
        raise ValueError(
            'analysis did not return a response: %s' % analysis_response)
    if 'results' not in analysis_response_json['response'].keys():
        raise ValueError('analysis did not receive any results: %s' %
                         analysis_response_json['response'])

    return analysis_response_json['response']['results']
