API = 'http://ip-api.com/json/'
REQUEST_TIMEOUT = 10  # seconds
DOMAINS = [
    # github
    'github.com',
    'github.io',
    'raw.githubusercontent.com',
    'central.github.com',
    'assets-cdn.github.com',
    'github.map.fastly.net',
    'github.global.ssl.fastly.net',
    'gist.github.com',
    'api.github.com',
    'codeload.github.com',
    'github-cloud.s3.amazonaws.com',
    'github-com.s3.amazonaws.com',
    'github-production-release-asset-2e65be.s3.amazonaws.com',
    'github-production-user-asset-6210df.s3.amazonaws.com',
    'github-production-repository-file-5c1aeb.s3.amazonaws.com',
    'githubstatus.com',
    'github.community',
    'raw.github.com',
    
    # python
    'docs.python.org',
    'python.org',

    # gravatar
    'gravatar.com',
    'cn.gravatar.com',
    's.gravatar.com',
    '2.gravatar.com',
    'pixel.wp.com',
]

HOSTS_PATTERN = r'# custom from ip-api start.+# custom from ip-api end'
