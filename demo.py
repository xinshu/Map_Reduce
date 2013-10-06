### demo.py

import glob
import mincemeat

text_files = glob.glob('test/*')

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

source = dict((file_name, file_contents(file_name))
              for file_name in text_files)

# setup map and reduce functions

def mapfn(key, value):
    for line in value.splitlines():
        for word in line.split():
            yield word.lower(), 1

def reducefn(key, value):
    return key, len(value)

# start the server

s = mincemeat.Server()
s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results


