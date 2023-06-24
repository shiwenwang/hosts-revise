import requests
import logging
from logging.handlers import RotatingFileHandler
from sys import platform
import re

from define import API, DOMAINS, HOSTS_PATTERN

logger = logging.getLogger('ip_query')
fh = RotatingFileHandler('hosts.log', maxBytes=1024 * 1024, backupCount=1)
fh.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
logger.addHandler(fh)
logger.setLevel(logging.INFO)


def query():
    hosts_lines = []
    for domain in DOMAINS:
        url = API + domain

        r = requests.get(url)
        if r.status_code != 200:
            logger.error(f'query {domain} failed, status: {r.status_code}')
        
        try:
            line = f'{r.json()["query"]} {domain}'
            logger.info(line)
            hosts_lines.append(line)
        except (UnicodeDecodeError, requests.exceptions.JSONDecodeError):
            logging.error('{domain} ip decode error')
        except KeyError as e:
            logging.error('{domain} ip : {e}')

    return hosts_lines

def _new_hosts(lines):
    data = '\n'.join(lines)
    return f"# custom from ip-api start\n{data}\n# custom from ip-api end\n"

def update_hosts(lines):
    """modify local hosts file
    """

    if platform == 'win32':
        hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
    elif platform == 'linux':
        hosts_path = '/etc/hosts'

    with open(hosts_path, 'r', encoding='utf-8') as f_in:
        origin = f_in.read()
    
    filemode = 'w'
    new_data = _new_hosts(lines)
    if '# custom from ip-api' not in origin:
        filemode = 'a+'
        new_data = '\n' + new_data
    else: 
        new_data = re.sub(HOSTS_PATTERN, new_data, origin, flags=re.DOTALL)
    
    with open(hosts_path, filemode, encoding='utf-8') as f_out:
        f_out.write(new_data)
