import requests
from django.conf import settings

BASE_URL = "https://ws.audioscrobbler.com/2.0/"

def fetch_lastfm(method, params=None):
    if params is None:
        params = {}
    
    api_key = getattr(settings, 'LASTFM_API_KEY', '')
    
    params.update({
        'method': method,
        'api_key': api_key,
        'format': 'json'
    })
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
    except requests.RequestException:
        pass
        
    return None