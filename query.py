import requests
from datetime import datetime
import re
import sys
from threading import Thread 

from define import API, REQUEST_TIMEOUT, DOMAINS, HOSTS_PATTERN
from logger import logger


class Query:
    def __init__(self, update) -> None:
        self._update_hosts = update
        self._dns_results = []

    def query(self):
        threads = []
        for domain in DOMAINS:
            threads.append(Thread(target=self.http_get, args=(domain, )))

        for t in threads:
             t.start()
        for t in threads:
             t.join()

        if self._update_hosts:
            self._update()

    def http_get(self, domain):
        r = requests.get(API + domain, timeout=REQUEST_TIMEOUT)
        if r.status_code != 200:
            logger.error(f'query {domain} failed, status: {r.status_code}')
            return
        
        result = r.json()
        ip, company = result['query'], result['as']
        logger.info(f'{domain} {ip} {company}')
        self._dns_results.append(f'{ip} {domain}')

    def _update(self):
        if sys.platform == 'win32':
            hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
        elif sys.platform == 'linux':
            hosts_path = '/etc/hosts'

        with open(hosts_path, 'r', encoding='utf-8') as f_in:
            origin = f_in.read()
        
        filemode = 'w'
        new_data = self._new_hosts_content()
        if '# custom from ip-api' not in origin:
            filemode = 'a+'
            new_data = '\n' + new_data
        else: 
            new_data = re.sub(HOSTS_PATTERN, new_data, origin, flags=re.DOTALL)
        
        with open(hosts_path, filemode, encoding='utf-8') as f_out:
            f_out.write(new_data)

        logger.info(f'\nUpdate done at {datetime.now()}.')
    
    def _new_hosts_content(self):
        self._dns_results.append(f'updated at {datetime.now()}')
        data = '\n'.join(self._dns_results)
        return f"# custom from ip-api start\n{data}\n# custom from ip-api end"
