
# This is an unwanted but committed change
import sys

name = sys.argv[1] if len(sys.argv) > 1 else 'World'
print 'Hello, %s!' % name
