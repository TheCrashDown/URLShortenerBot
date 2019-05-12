import requests


def get_qr_code(text):
    '''
    Function that recieves qr pic using qrserver api

    Args:
        source text

    Returns:
        none (picture with qr code is saved in "img.jpg")
    '''
    _url = 'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=' + text

    resp = requests.get(_url)

    return resp.content
