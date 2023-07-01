from query import Query
import sys

update_hosts =  len(sys.argv) > 1 and sys.argv[1] == '-u'
Query(update_hosts).query()
