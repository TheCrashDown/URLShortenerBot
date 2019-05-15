import requests


def get_shorten_url(longUrl):
    '''
    Function that recieves shorten url using cleanuri.com api

    Args:
        source url

    Returns:
        bool value - flag shows was convertion succesfull or not
        string - shorten url, if succesfull        
    '''
    _url = 'https://cleanuri.com/api/v1/shorten'

    if not longUrl.startswith(('https://', 'http://')):
        longUrl = 'http://' + longUrl

    resp = requests.post(_url, data={'url': longUrl}).json()

    return resp
