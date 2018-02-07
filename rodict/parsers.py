import json

def json_parser(file_name):
    f = open(file_name, 'r')
    file_data = f.read()
    data_dict = json.loads(file_data)
    return data_dict