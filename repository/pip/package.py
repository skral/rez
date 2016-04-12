name = "pip"
version = '8.1.1'
authors = ['The pip developers']
uuid = "d9770af0-ea32-11e5-a5c5-0025902178a3"
description = 'The PyPA recommended tool for installing Python packages.'
homepage = 'https://pip.pypa.io'

tools = ['pip']

requires = ['python']

variants = [['platform-windows', 'arch-AMD64', 'os-windows-6.1.7601.SP1']]


def commands():
    env.PATH.append('{this.root}/bin')
    env.PYTHONPATH.append('{this.root}/python')
