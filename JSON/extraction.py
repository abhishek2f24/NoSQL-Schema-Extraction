import json
JSON = open('example.json')
data_dictionary = json.load(JSON)
def func(dictionary, depth):
    list_keys = []
    def deep_keys(dictionary):
        if not isinstance(dictionary, (dict, list)):
            return ['']
        if isinstance(dictionary, list):
            return [keys for sub_level in dictionary for keys in deep_keys(sub_level)]
        return [key+('.'+keys if keys else '') for key, value in dictionary.items() for keys in deep_keys(value)]
    if depth==1:
        for key in dictionary.keys(): 
            list_keys.append(key)
        return list_keys
    else:
        result = deep_keys(dictionary)
        for i in result:
            if i.count('.')<=depth:
                print(i)
list_of_keys = func(data_dictionary,2) #value 2 should be replaced with depth till you want the schema
print(list_of_keys)
