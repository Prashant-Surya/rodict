##RoDict

A python package for accessing internal keys of a dictionary easily. RoDict internally stores the data as a dictionary.

Any internal keys of a dictionary by using a key by separating the nested keys using a separator. Default separator is `__` (two underscores).

For example consider the following dictionary:

```python
data = {
	'a' : {
		'b': {
			'c': 10
		}
	}
}
```

**Accessing value of key 'c' in the above dictionary:**

#### Without RoDict 

```python
>>> data = data['a']
>>> data = data['b']
>>> data = data['c']
>>> print data
```

#### With RoDict

```python
>>> from rodict import RoDict
>>> r = RoDict(store=data)
>>> print r['a__b__c']
```

Not only for getting values, setting values for a key in dict can be done using the same syntax.

### Where can it be used:

Right now I'm using this package for maintaining/updating configuration files in `json` where values need to be dynamically updating during runtime.


## Installation:

For contribution:

```bash
$ git clone git@github.com:Prashant-Surya/rodict.git
$ cd rodict
$ python setup.py develop
```

Just for using it as a package:

```bash
$ git clone git@github.com:Prashant-Surya/rodict.git
$ cd rodict
$ python setup.py install
```

## Contribution:

1. For contributing to the RoDict create a fork from this repo.
2. Work on a feature branch.
3. Raise a Pull Request to the master branch of this repo.
