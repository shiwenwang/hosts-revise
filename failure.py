import os

_THIS_DIR = os.path.dirname(__file__)
_FAILURE_DIR = os.path.join(_THIS_DIR, 'fail')

def failure_handler(hostname, req):
    print(f'Get ip adress of {hostname} failed')
    if not os.path.isdir(_FAILURE_DIR):
        os.makedirs(_FAILURE_DIR)
    f = open(os.path.join(_FAILURE_DIR, f'{hostname}.html'), \
        'w', encoding='utf-8')
    f.write(req.text)
    f.close()
