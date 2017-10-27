# Default is World
# Author: Jim Weirich (jim@somewhere.com)
import sys

name = sys.argv[1] if len(sys.argv) > 1 else 'World'
print 'Hello, %s!' % name
