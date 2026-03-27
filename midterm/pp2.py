import json 
import re 
a = '{"Asyl": "asylzhansei%tker@gmail.com", "Aknur":"efvdf$9.com"}'
b = json.loads(a)
for name, email in b.items():
        if re.fullmatch(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email):
                print(name)