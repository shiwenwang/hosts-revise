# github-hosts

A very simple tool to query the real IP addresses of domains which polluted by DNS cache poisoning.


# Usage

## Query Only
```bash
# python .

140.82.112.4 github.com
185.199.108.153 github.io
2606:50c0:8002::154 raw.githubusercontent.com
140.82.112.22 central.github.com
2606:50c0:8001::153 assets-cdn.github.com
185.199.110.133 github.map.fastly.net
151.101.65.194 github.global.ssl.fastly.net
192.30.255.112 gist.github.com
192.30.255.117 api.github.com
140.82.113.10 codeload.github.com
52.217.136.129 github-cloud.s3.amazonaws.com
52.217.173.81 github-com.s3.amazonaws.com
54.231.164.217 github-production-release-asset-2e65be.s3.amazonaws.com
52.216.222.169 github-production-user-asset-6210df.s3.amazonaws.com
52.217.12.164 github-production-repository-file-5c1aeb.s3.amazonaws.com
185.199.110.153 githubstatus.com
140.82.112.18 github.community
2606:50c0:8001::154 raw.github.com
```


## Update hosts file
```bash
python . -u
```

# Acknowledgement
This software uses [IP-API](https://ip-api.com/).
