FROM python:3.11.0-alpine3.15
COPY . /app
WORKDIR /app
CMD pip install requests pyyaml && python dns_query.py
