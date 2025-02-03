import requests

# Call the API to get IP address details for the given ip (API returns a JSON dump)
def get_ip_details(ip_addr):
    request_url=f'https://api.ipquery.io/{ip_addr}?format=json'
    ip_detail_dump = requests.get(request_url).json()
    return ip_detail_dump

# Call the API to get the default IP address (API returns a JSON dump)
def get_default_ip_details():
    request_url=f'https://api.ipquery.io/?format=json'
    ip_detail_dump = requests.get(request_url).json()
    return ip_detail_dump


