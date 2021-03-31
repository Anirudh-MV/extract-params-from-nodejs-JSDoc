import re
import json
s = open('file.txt').read()
body = []
params = []
query = []
for line in s.splitlines():
    res = re.findall( r"req\.body\.(\w+)", line)
    body.extend(res)
    params.extend(res)
    res = re.findall( r"req\.params\.(\w+)", line)
    params.extend(res)
    res = re.findall( r"req\.query\.(\w+)", line)
    query.extend(res)
d = {}
pre = ""
for i in body:
    d[i] = "{{" + i + "}}"
params.extend(query)
params = list(set(params))
query = list(set(query))
for i in params:
    pre += " * @param {string} " + i + " - The " + i + "\n"
querys = "?"
for i in query:
    querys += i + "=" + "{{" + i + "}}" + "&"

print("The body as JSON")
json_txt = json.dumps(d, indent=3, sort_keys=True)
json_txt = json_txt.replace('"{{', '{{').replace('}}"', '}}')
print(json_txt)

print()
print("JSDocs format params with all 3 parameters (url param, query param and body param)")
print(pre)

print()
print("The query string")
print(querys)
