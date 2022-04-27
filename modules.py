# https://docs.python.org/3/py-modindex.html

import sys
from random import randint as gera

print(sys.platform)

for v in range(10):
    print(gera(0, 10))