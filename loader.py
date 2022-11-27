import os
import yaml

_THIS_DIR = os.path.dirname(__file__)

class Loader:
    def __init__(self) -> None:
        self._config_file = os.path.join(_THIS_DIR, 'hosts.yaml')
        self._load()

    def _load(self):
        with open(self._config_file, 'r', encoding='utf-8') as stream:
            hostnames = yaml.load(stream, Loader=yaml.Loader)

        self._hostnames = hostnames['hosts']
        self._source = hostnames['source']
    
    @property
    def source(self):
        return self._source

    @property
    def hostnames(self):
        return self._hostnames

name_loader = Loader()
