import json

def json_parser(file_name):
    f = open(file_name, 'r')
    file_data = f.read()
    f.close()
    data_dict = json.loads(file_data)
    return data_dict

class Parser(object):

    def read(self):
        pass

    def write(self):
        pass


class JSONParser(Parser):
    '''Parser for reading json files and processing them.
    This also includes writing the files to disk after processing is done.
    '''
    def read(self, file_name):
        self.input_file = file_name
        f = open(file_name, 'r')
        file_data = f.read()
        f.close()
        return json.loads(file_data)

    def write(self, file_name=None, data={}):
        if not file_name:
            file_name, ext = self.input_file.split('.')
            file_name = file_name + '-processed.' + ext
        f = open(file_name, 'w')
        f.write(json.dumps(data, sort_keys=True, indent=2))
        f.close()