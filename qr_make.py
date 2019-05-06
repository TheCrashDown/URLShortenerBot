import requests


def get_qr_code(text):
    '''
    Function that recieves qr pic using qrserver api

    Args:
        source text

    Returns:

    '''
    _url = 'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=' + text

    resp = requests.get(_url)

    with open("img.jpg", 'wb') as f:
        f.write(resp.content)
