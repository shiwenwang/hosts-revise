# github-hosts
A python tool that gets github related ip addresses.

# Usage

## Get hostname and ipv4 address pairs to stdout
```shell
python dns_query.py
```


## Update the system hosts file

```shell
python dns_query.py -u
```

## Save hostname and ipv4 address pairs to a file

```shell
python dns_query.py -o <file-path>
```


# Example

```shell
# python .\dns_query.py

# === Github DNS Start ===
140.82.114.4    github.com
185.199.109.153 github.io
185.199.108.133 raw.githubusercontent.com
185.199.109.133 raw.githubusercontent.com
185.199.110.133 raw.githubusercontent.com
185.199.111.133 raw.githubusercontent.com
140.82.113.21   central.github.com
185.199.109.153 assets-cdn.github.com
185.199.108.133 github.map.fastly.net
185.199.109.133 github.map.fastly.net
185.199.110.133 github.map.fastly.net
185.199.111.133 github.map.fastly.net
151.101.1.194   github.global.ssl.fastly.net
151.101.65.194  github.global.ssl.fastly.net
151.101.129.194 github.global.ssl.fastly.net
151.101.193.194 github.global.ssl.fastly.net
140.82.113.3    gist.github.com
140.82.113.5    api.github.com
140.82.113.10   codeload.github.com
3.5.16.111      github-cloud.s3.amazonaws.com
52.216.138.155  github-cloud.s3.amazonaws.com
52.216.144.227  github-cloud.s3.amazonaws.com
52.216.176.27   github-cloud.s3.amazonaws.com
52.216.217.209  github-cloud.s3.amazonaws.com
52.217.82.52    github-cloud.s3.amazonaws.com
52.217.139.41   github-cloud.s3.amazonaws.com
52.217.199.41   github-cloud.s3.amazonaws.com
52.216.24.36    github-com.s3.amazonaws.com
52.216.200.163  github-com.s3.amazonaws.com
52.217.192.33   github-com.s3.amazonaws.com
52.217.197.145  github-com.s3.amazonaws.com
52.217.228.177  github-com.s3.amazonaws.com
52.217.230.97   github-com.s3.amazonaws.com
54.231.195.25   github-com.s3.amazonaws.com
54.231.200.137  github-com.s3.amazonaws.com
3.5.1.132       github-production-release-asset-2e65be.s3.amazonaws.com
3.5.19.145      github-production-release-asset-2e65be.s3.amazonaws.com
52.216.54.1     github-production-release-asset-2e65be.s3.amazonaws.com
52.217.67.92    github-production-release-asset-2e65be.s3.amazonaws.com
52.217.137.129  github-production-release-asset-2e65be.s3.amazonaws.com
52.217.166.25   github-production-release-asset-2e65be.s3.amazonaws.com
52.217.194.177  github-production-release-asset-2e65be.s3.amazonaws.com
52.217.235.249  github-production-release-asset-2e65be.s3.amazonaws.com
3.5.17.197      github-production-user-asset-6210df.s3.amazonaws.com
52.216.217.121  github-production-user-asset-6210df.s3.amazonaws.com
52.216.241.44   github-production-user-asset-6210df.s3.amazonaws.com
52.217.13.236   github-production-user-asset-6210df.s3.amazonaws.com
52.217.72.20    github-production-user-asset-6210df.s3.amazonaws.com
52.217.136.241  github-production-user-asset-6210df.s3.amazonaws.com
54.231.136.209  github-production-user-asset-6210df.s3.amazonaws.com
54.231.170.177  github-production-user-asset-6210df.s3.amazonaws.com
3.5.0.211       github-production-repository-file-5c1aeb.s3.amazonaws.com
52.217.0.188    github-production-repository-file-5c1aeb.s3.amazonaws.com
52.217.44.100   github-production-repository-file-5c1aeb.s3.amazonaws.com
52.217.98.212   github-production-repository-file-5c1aeb.s3.amazonaws.com
52.217.136.249  github-production-repository-file-5c1aeb.s3.amazonaws.com
52.217.166.17   github-production-repository-file-5c1aeb.s3.amazonaws.com
52.217.195.1    github-production-repository-file-5c1aeb.s3.amazonaws.com
54.231.162.177  github-production-repository-file-5c1aeb.s3.amazonaws.com
185.199.109.153 githubstatus.com
140.82.112.18   github.community
185.199.108.133 raw.github.com
185.199.109.133 raw.github.com
185.199.110.133 raw.github.com
185.199.111.133 raw.github.com
# Update at 2022-11-27 17:22:46
# === Github DNS End ===

```
