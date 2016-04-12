name = "ordereddict"
authors = ["Raymond Hettinger", "Steven Hazel"]
version = '1.1'
uuid = "5a99a38a-cfd4-11e2-afe2-001d4f455738"
description = "A drop-in substitute for Py2.7's new collections.OrderedDict that works in Python 2.4-2.6."
homepage = "https://pypi.python.org/pypi/ordereddict"

requires = ['python']

build_requires = ['cmake', 'msvc-9', 'pip']

def commands():
    env.PYTHONPATH.append('{this.root}/python')
