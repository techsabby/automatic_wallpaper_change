import requests

api_url_base = "http://api.weatherapi.com/v1"
api_url_json = "current.json?"
api_key = "key=11151e2b5f9241d091b214318230409"
full_url = "http://api.weatherapi.com/v1/current.json?key=11151e2b5f9241d091b214318230409&q=New_York"

def get_condition():
    response = requests.get(full_url)
    api_json = response.json()
    data = api_json['current']
    data_extracted = data['condition']
    code = data_extracted['code']
    
    return code 
    