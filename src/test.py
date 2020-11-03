import sys, os

print("script: sys.argv[0] is", repr(sys.argv[0]))
print("script: __file__ is", repr(__file__))
print("script: cwd is", repr(os.getcwd()))

import pathlib

print(pathlib.Path(__file__).parent.absolute())