import json
with open('filename.json',  encoding='') as new_dict: #encoding values can be one of the ascii, utf-8-sig, latin1 and many more
    for lines in new_dict.readlines():
        res = json.loads(lines)
        json_schema = []
        for key in res:
            json_schema.append(key)
print(set(json_schema))
