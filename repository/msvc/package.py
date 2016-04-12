name = "msvc"
version = '9.0'
authors = ['Microsoft']
uuid = "3ca31080-e9ff-11e5-a593-0025902178a3"
description = 'This package contains the compiler and set of system headers necessary for producing binary wheels for Python 2.7 packages.'
homepage = 'https://www.microsoft.com/en-us/download/details.aspx?id=44266'

variants = [['platform-windows', 'arch-AMD64', 'os-windows-6.1.7601.SP1', 'target-AMD64', 'python-2.7'],
            ['platform-windows', 'arch-AMD64', 'os-windows-6.1.7601.SP1', 'target-AMD86', 'python-2.7']]


def commands():
    """Taken from vcvarsall.bat
    """

    env.VCINSTALLDIR = '{this.root}/VC/'
    env.WindowsSdkDir = '{this.root}/WinSDK/'

    path_vc = '{this.root}/VC/Bin'
    path_winsdk = '{this.root}/WinSDK/Bin'
    include_vc = '{this.root}/VC/Include'
    include_winsdk = '{this.root}/WinSDK/Include'
    lib_vc = '{this.root}/VC/Lib'
    lib_winsdk = '{this.root}/WinSDK/Lib'

    if env.REZ_TARGET_VERSION == "AMD64":
        path_vc += '/amd64'
        lib_vc += '/amd64'
        lib_winsdk += '/x64'
        env.PATH.prepend(path_winsdk + '/x64')

    env.PATH.prepend(path_winsdk)
    env.PATH.prepend(path_vc)
    env.INCLUDE.prepend(include_winsdk)
    env.INCLUDE.prepend(include_vc)
    env.LIB.prepend(lib_winsdk)
    env.LIB.prepend(lib_vc)
    env.LIBPATH.prepend(lib_winsdk)
    env.LIBPATH.prepend(lib_vc)
