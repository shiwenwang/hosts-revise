import re

IPV4_PATTERN = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

DOMIN_PATTERN = re.compile(
    r'<ul class="comma-separated">'\
        r'<li>'\
            f'({IPV4_PATTERN})'\
        r'</li>'\
    r'</ul>')

DNS_LOOKUP_PATTERN = re.compile(
    rf'<td>A</td><td><a href=[^<>]+>({IPV4_PATTERN})</a>')

UPDATE_PATTERN = re.compile(
    '# === Github DNS Start ===.*=== Github DNS End ===', 
    re.DOTALL)
