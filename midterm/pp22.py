import json 
import re 
a = input()
b = json.loads(a)
for id, handle in b:
    c = id['handle']
    if re.match(r'^@(?=[a-z_]*_[a-z_]+$', c):
        print(id)