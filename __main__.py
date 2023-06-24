import query
import sys

lines = query.query()
print('\n'.join(lines))

if len(sys.argv) > 1 and sys.argv[1] == '-u':
    query.update_hosts(lines)
