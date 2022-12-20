import requests
import pytest

def test_httpbin():
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=DEMO_KEY'
    r = requests.get(url=url)
    print (r.json())

