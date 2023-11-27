import requests


def check_valid_url(url):
    try:
        requests.get(url)
        return True
    except:
        return False
