import json
import requests


def _get_scan_id_list(scan_array: list) -> list:
    return list(map(lambda scan: scan['id'], scan_array))


def sc_get_scans(headers: dict, cookies: str, sc_base_uri: str) -> list:
    '''
    Retrieves a list of scan results from Tenable Security Center, then returns a list of
    the scan IDs. The greater the scan ID, the more recent the scan.
    '''

    if not headers or not cookies or not sc_base_uri:
        raise TypeError(
            'Missing parameter(s): headers, cookies, sc_base_uri, or provided to get_scans')

    scan_result_response = requests.get(
        sc_base_uri + '/rest/scanResult', cookies=cookies,
        headers=headers, verify=False)

    scan_result_json = scan_result_response.json()

    if 'response' not in scan_result_json.keys():
        raise ValueError(
            'analysis did not return a response: %s' % scan_result_json)
    if 'usable' not in scan_result_json['response'].keys():
        raise ValueError('get_scans received a malformed response: %s' %
                         scan_result_json['response'])

    scan_ids = _get_scan_id_list(scan_result_json['response']['usable'])
    return scan_ids
