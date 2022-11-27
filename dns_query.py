import requests
from pattern import DOMIN_PATTERN, DNS_LOOKUP_PATTERN
from loader import name_loader 
from failure import failure_handler
from sys import platform
import argparse
from datetime import datetime


class DNSQuery:
    def __init__(self) -> None:
        self._hosts_content = '# === Github DNS Start === \n'

    def query(self):
        print('Query...')
        for hostname in name_loader.hostnames:
            r = requests.get(name_loader.source + hostname)
            m = DOMIN_PATTERN.search(r.text)

            try:
                self._hosts_content += f'{m.group(1)}\t{hostname}\n'
            except AttributeError:
                m = DNS_LOOKUP_PATTERN.findall(r.text)
                if not len(m):
                    failure_handler(hostname, r)
                    continue
                self._hosts_content += ''.join([f'{addr}\t{hostname}\n' for addr in m])
            except AttributeError:
                    failure_handler(hostname, r)

        self._hosts_content += f'Update at {datetime.now().strftime("%F %T")}\n'
        self._hosts_content += '# === Github DNS End === '


    def dump(self, of):
        if of is None:
            print(self._hosts_content)
            return

        with open(of, 'w', encoding='utf-8') as f:
            f.write(self._hosts_content)


    def update_hosts(self):
        import os
        import shutil

        if platform == 'win32':
            hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
        elif platform == 'linux':
            hosts_path = '/etc/hosts'

        bak = os.path.join(os.path.dirname(hosts_path), 'hosts.bak_bef_upd')
        if not os.path.isfile(bak):
            shutil.copy(hosts_path, bak)
            
        with open(hosts_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        self.__update(content, hosts_path)

    
    def __update(self, content, hosts_path):
        from pattern import UPDATE_PATTERN

        if '=== Github DNS Start ===' in content:
            UPDATE_PATTERN.sub(self._hosts_content, content)
        else:
            content += '\n\n' + self._hosts_content + '\n\n'
                
        with open(hosts_path, 'w', encoding='utf-8') as f:
            f.write(content)


class Launcher:
    def __init__(self) -> None:
        self._argparser_init()
        self._args = None

    def _argparser_init(self):
        self._parser = argparse.ArgumentParser()
        self._parser.add_argument(
            '-u', '--update', action='store_true',
            help='update the hosts file on the local machine')
        self._parser.add_argument(
            '-o', '--output',
            help="sink hosts content to stdout(default) or a file")

    def parse(self):
        self._args = self._parser.parse_args()

    
    @property
    def update_hosts(self):
        return self._args.update is not None

    @property
    def output(self):
        return self._args.output


if __name__ == '__main__':
    app = Launcher()
    app.parse()

    dns = DNSQuery()
    dns.query()

    dns.dump(app.output)
    if app.update_hosts:
        dns.update_hosts()
