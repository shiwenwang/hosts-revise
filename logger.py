
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('ip_query')
fh = RotatingFileHandler('hosts.log', maxBytes=1024 * 1024, backupCount=1)
fh.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
logger.addHandler(fh)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)
