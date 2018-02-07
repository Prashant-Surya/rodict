from collections import MutableMapping

from rodict.constants import SUPPORTED_FILE_FORMATS, PARSER_FROM_EXTENSION

class RoDict(MutableMapping):

    # Default separator for the RoDict is ___ (three underscores)
    # It can be changed based on the special chars used in the keys of the 
    # dictionary.
    SEPARATOR = "___"

    def __init__(self, *args, **kwargs):
        '''Initializes a new RoDict with the contents of a
        file. If contents cannot be converted into a dictionary it'll fail.
        '''
        file_name = kwargs.get('file_name')
        self.store = {}
        if file_name:
            file_ext = file_name.split(".")[-1]
            if not file_ext or (file_ext not in SUPPORTED_FILE_FORMATS):
                raise Exception("Invalid file extension supplied. Supports only " + ' '.join(SUPPORTED_FILE_FORMATS))
            parser = PARSER_FROM_EXTENSION[file_ext]
            data_dict = parser(file_name)
            self.store = data_dict

    def __getitem__(self, key):
        if not self.SEPARATOR in key:
            return self.store[key]
        keys = key.split(self.SEPARATOR)
        data = self.store
        for key in keys:
            data = data[key]
        return data

    def __goto(self, keys):
        data = self.store
        for i in range(0, len(keys)-1):
            data = data[keys[i]]
        return data

    def __setitem__(self, key, value):
        if not self.SEPARATOR in key:
            self.store[key] = value
        keys = key.split(self.SEPARATOR)
        data = self.store
        for i in range(0, len(keys)-1):
            data = data[keys[i]]
        data[keys[-1]] = value
    
    def __len__(self):
        return len(self.store)

    def __delitem__(self, key):
        if not self.SEPARATOR in key:
            del self.store[key]
        else:
            keys = key.split(self.SEPARATOR)
            data = self.store
            for i in range(0, len(keys)-1):
                data = data[keys[i]]
            del data[keys[-1]]

    def __keytransform__(self, key):
        return key

    def __iter__(self):
        return iter(self.store)