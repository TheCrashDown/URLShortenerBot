class Messages:
    '''
    Container with different messages
    '''
    start = ('Hello there! This is URL Shortener Bot.\n\n'
             'Here is the list of availible commands:\n'
             '/start - see this message\n'
             '/url *your url* - shorten long url to nice and '
             'compact one\n'
             'also availible forms - /sh and /shorten\n'
             '/qr *your text* - convert your text to QR pic')
    invalid_url = ('OOops...\nSeems like your URL is invalid.\n'
                   'Make sure your link looks like that:'
                   ' https://example.com/')
    sh_succ = ('Here is your shortened link:\n')
