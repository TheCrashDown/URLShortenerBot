import requests
import time
from res import Messages
from url_sh import get_shorten_url
from qr_make import get_qr_code


TOKEN = ''
tg_url = 'https://api.telegram.org/bot' + TOKEN + '/'


def get_updates():
    '''
    Function that recieves last updates from Telegram

    Args:
        none

    Returns:
        json dict with last updates
    '''
    _url = tg_url + 'getUpdates'
    resp = requests.get(_url).json()
    return resp


def parse_resp(resp):
    '''
    Function that takes last message from updates and
        extracts important indormation

    Args:
        json dict with last updates

    Returns:
        dict with chat id, message_id and message text of last message 
    '''
    message = {}

    try:
        message['chat_id'] = resp['result'][-1]['message']['chat']['id']
        message['message_id'] = resp['result'][-1]['update_id']
        message['text'] = resp['result'][-1]['message']['text']

    except IndexError:
        pass  # if no messages yet

    return message


def send_message(chat, text):
    '''
    Function that sends message to Telegram with chat_id and text from args

    Args:
        chat_id
        message text

    Returns:
        none
    '''
    _url = tg_url + 'sendMessage?chat_id={}&text={}'.format(chat, text)

    requests.get(_url)


def send_pic(chat, img):
    '''
    Function that sends image to Telegram with chat_id
    '''
    content = {'photo': img}

    _url = tg_url + 'sendPhoto?chat_id={}'.format(chat)

    requests.post(_url, files=content)


def cmd_start(parsed):
    '''
    Function that sends greeting message
    '''
    send_message(parsed['chat_id'], Messages.start)


def cmd_shorten(parsed):
    '''
    Function that shortens source URL and sends it to user
    '''
    space = parsed['text'].find(' ')
    source_url = parsed['text'][space::].strip()
    res = get_shorten_url(source_url)

    if 'result_url' in res:
        send_message(parsed['chat_id'], Messages.sh_succ + res['result_url'])
    else:
        send_message(parsed['chat_id'], Messages.invalid_url)


def cmd_qr_code(parsed):
    '''
    Function that creates qr pic and sends it to user
    '''
    space = parsed['text'].find(' ')
    source = parsed['text'][space::].strip()

    img = get_qr_code(source)

    send_message(parsed['chat_id'], Messages.qr_succ)
    send_pic(parsed['chat_id'], img)


if __name__ == '__main__':
    '''
    Main function, that recieves and sends messages to user
    '''
    TOKEN = str(open("token.txt", "r").read()).strip()

    last_answered = 0  # id of last answered message

    while True:
        time.sleep(1)

        resp = get_updates()
        parsed = parse_resp(resp)

        # if last message is already answered
        if last_answered == parsed['message_id']:
            continue

        if '/start' in parsed['text']:
            cmd_start(parsed)

        if parsed['text'].startswith(('/url ', '/sh ', '/shorten ')):
            cmd_shorten(parsed)

        if parsed['text'].startswith('/qr'):
            cmd_qr_code(parsed)

        last_answered = parsed['message_id']
