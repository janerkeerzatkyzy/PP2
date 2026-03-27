import ast, re

s = input().strip()
s1 = ast.literal_eval(s)

for i in s1:
    handle = i['handle']
    if re.fullmatch(r'@[a-z_]+', handle):
        print(i['user_id'])