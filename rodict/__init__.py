import json
from collections import MutableMapping

from rodict.constants import SUPPORTED_FILE_FORMATS, PARSER_FROM_EXTENSION

class RoDict(MutableMapping):

    # Default separator for the RoDict is __ (two underscores)
    # It can be changed based on the special chars used in the keys of the 
    # dictionary.
    SEPARATOR = "__"
    parser = None

    def __init__(self, *args, **kwargs):
        '''Initializes a new RoDict with the contents of a
        file. If contents cannot be converted into a dictionary it'll fail.
        '''
        file_name = kwargs.get('file_name')
        self.file_name = file_name
        self.store  = kwargs.get('store', {})

        if file_name:
            file_ext = file_name.split(".")[-1]
            if not file_ext or (file_ext not in SUPPORTED_FILE_FORMATS):
                raise Exception("Invalid file extension supplied. Supports only " + ' '.join(SUPPORTED_FILE_FORMATS))
            self.parser = PARSER_FROM_EXTENSION[file_ext]()
            data_dict = self.parser.read(file_name)
            self.store = data_dict

    def __goto(self, keys):
        data = self.store
        for key in keys:
            if '[' in key:
                temp_key = key.split('[')
                # Get the value of the dictionary which must be an iterable
                data = data[temp_key[0]]
                # Strip away the trailing ]
                filter_key = temp_key[1].rstrip(']')
                # Get key, value from filter_key
                tkey, tvalue = filter_key.split('=')
                val = list(filter(lambda k: k[tkey] == tvalue, data))
                data = val[0]
            else:
                data = data[key]
        return data

    def __getitem__(self, key):
        if key.endswith(']'):
            item = self.__goto([key])
        elif not self.SEPARATOR in key:
            item = self.store[key]
        else:
            keys = key.split(self.SEPARATOR)
            item = self.__goto(keys)
        if type(item) == dict:
            return RoDict(store=item)
        return item

    def __setitem__(self, key, value):
        if not self.SEPARATOR in key:
            self.store[key] = value
        keys = key.split(self.SEPARATOR)
        # Getting the last dictionary by passing the 1st to last but one keys
        data = self.__goto(keys[:-1])
        data[keys[-1]] = value
    
    def __len__(self):
        return len(self.store)

    def __delitem__(self, key):
        if not self.SEPARATOR in key:
            del self.store[key]
        else:
            keys = key.split(self.SEPARATOR)
            data = self.__goto(keys[:-1])
            del data[keys[-1]]

    def __keytransform__(self, key):
        return key

    def __iter__(self):
        return iter(self.store)

    def __unicode__(self):
        return str(self.store)

    def __str__(self):
        return str(self.store)

    def write(self):
        if self.parser:
            self.parser.write(data=self.store)
        else:
            raise NotImplementedError("Parser not implemented")